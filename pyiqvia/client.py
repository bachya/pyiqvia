"""Define a client to interact with Pollen.com."""
import asyncio
from typing import Optional
from urllib.parse import urlparse

from aiohttp import ClientSession
from async_timeout import timeout

from .allergens import Allergens
from .asthma import Asthma
from .const import LOGGER
from .disease import Disease
from .errors import InvalidZipError, RequestError

DEFAULT_REQUEST_RETRY_INTERVAL = 3
DEFAULT_RETRIES = 3
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
        request_retries: int = DEFAULT_RETRIES,
        request_retry_interval: int = DEFAULT_REQUEST_RETRY_INTERVAL,
        request_timeout: int = DEFAULT_TIMEOUT,
        session: Optional[ClientSession] = None,
    ) -> None:
        """Initialize."""
        if not is_valid_zip_code(zip_code):
            raise InvalidZipError(f"Invalid ZIP code: {zip_code}")

        self._request_retries = request_retries
        self._request_retry_interval = request_retry_interval
        self._request_timeout = request_timeout
        self._session: ClientSession = session
        self.zip_code = zip_code

        self.allergens = Allergens(self._request)
        self.asthma = Asthma(self._request)
        self.disease = Disease(self._request)

    async def _request(
        self,
        method: str,
        url: str,
        *,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        json: Optional[dict] = None,
    ) -> dict:
        """Make a request against AirVisual."""
        pieces = urlparse(url)

        _headers = headers or {}
        _headers.update(
            {
                "Content-Type": "application/json",
                "Referer": f"{pieces.scheme}://{pieces.netloc}",
                "User-Agent": DEFAULT_USER_AGENT,
            }
        )

        use_running_session = self._session and not self._session.closed

        if use_running_session:
            session = self._session
        else:
            session = ClientSession()

        retry = 0

        while retry < self._request_retries:
            try:
                async with timeout(self._request_timeout), session.request(
                    method,
                    f"{url}/{self.zip_code}",
                    headers=_headers,
                    params=params,
                    json=json,
                ) as resp:
                    resp.raise_for_status()
                    data = await resp.json(content_type=None)

                    LOGGER.debug("Received data for %s: %s", url, data)

                    return data
            except Exception as err:  # pylint: disable=broad-except
                LOGGER.warning(
                    "Error while requesting %s: %s (attempt %s of %s)",
                    url,
                    err,
                    retry + 1,
                    self._request_retries,
                )
                retry += 1
                await asyncio.sleep(self._request_retry_interval)
            finally:
                if not use_running_session:
                    await session.close()

        raise RequestError(f"Requesting {url} failed after {retry} tries") from None
