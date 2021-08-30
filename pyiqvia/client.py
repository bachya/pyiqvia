"""Define a client to interact with IQVIA."""
import asyncio
import logging
import sys
from typing import Any, Dict, Optional, cast
from urllib.parse import urlparse

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError
import backoff

from .allergens import Allergens
from .asthma import Asthma
from .disease import Disease
from .errors import InvalidZipError, RequestError

_LOGGER = logging.getLogger(__package__)

DEFAULT_RETRIES = 4
DEFAULT_TIMEOUT = 3
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) "
    + "AppleWebKit/537.36 (KHTML, like Gecko) "
    + "Chrome/65.0.3325.181 Safari/537.36"
)


def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid."""
    return len(zip_code) == 5 and zip_code.isdigit()


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(
        self,
        zip_code: str,
        *,
        session: Optional[ClientSession] = None,
        request_retries: int = DEFAULT_RETRIES,
        logger: Optional[logging.Logger] = None,
    ) -> None:
        """Initialize."""
        if not is_valid_zip_code(zip_code):
            raise InvalidZipError(f"Invalid ZIP code: {zip_code}")

        self._session = session
        self.zip_code = zip_code

        if logger:
            self._logger = logger
        else:
            self._logger = _LOGGER

        # Implement a version of the request coroutine, but with backoff/retry logic:
        self.async_request = backoff.on_exception(
            backoff.expo,
            (asyncio.TimeoutError, ClientError),
            logger=self._logger,
            max_tries=request_retries,
            on_giveup=self._handle_on_giveup,
        )(self._async_request)

        self.allergens = Allergens(self.async_request)
        self.asthma = Asthma(self.async_request)
        self.disease = Disease(self.async_request)

    async def _async_request(
        self, method: str, url: str, **kwargs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Make a request against the IQVIA API."""
        url_pieces = urlparse(url)
        kwargs.setdefault("headers", {})
        kwargs["headers"]["Content-Type"] = "application/json"
        kwargs["headers"]["Referer"] = f"{url_pieces.scheme}://{url_pieces.netloc}"
        kwargs["headers"]["User-Agent"] = DEFAULT_USER_AGENT

        use_running_session = self._session and not self._session.closed

        if use_running_session:
            session = self._session
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        assert session

        async with session.request(method, f"{url}/{self.zip_code}", **kwargs) as resp:
            resp.raise_for_status()
            data = await resp.json()

        if not use_running_session:
            await session.close()

        self._logger.debug("Received data for %s: %s", url, data)

        return cast(Dict[str, Any], data)

    @staticmethod
    def _handle_on_giveup(_: Dict[str, Any]) -> None:
        """Wrap a giveup exception as a RequestError."""
        err_info = sys.exc_info()
        err = err_info[1].with_traceback(err_info[2])  # type: ignore
        raise RequestError(err) from err
