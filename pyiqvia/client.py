"""Define a client to interact with IQVIA."""
from __future__ import annotations

import asyncio
import logging
import sys
from collections.abc import Awaitable, Callable
from typing import Any, cast
from urllib.parse import urlparse

import backoff
from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError

from .allergens import Allergens
from .asthma import Asthma
from .const import LOGGER
from .disease import Disease
from .errors import InvalidZipError, RequestError

DEFAULT_RETRIES = 4
DEFAULT_TIMEOUT = 3
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) "
    + "AppleWebKit/537.36 (KHTML, like Gecko) "
    + "Chrome/65.0.3325.181 Safari/537.36"
)


def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid.

    Args:
        zip_code: A ZIP code

    Returns:
        Whether the ZIP code is valid.
    """
    return len(zip_code) == 5 and zip_code.isdigit()


class Client:
    """Define the client."""

    def __init__(
        self,
        zip_code: str,
        *,
        logger: logging.Logger | None = None,
        request_retries: int = DEFAULT_RETRIES,
        session: ClientSession | None = None,
    ) -> None:
        """Initialize.

        Args:
            zip_code: A ZIP code.
            logger: An option logger.
            request_retries: The number of retries to give a failed request.
            session: An optional aiohttp ClientSession.

        Raises:
            InvalidZipError: Raised on an invalid ZIP code.
        """
        if not is_valid_zip_code(zip_code):
            raise InvalidZipError(f"Invalid ZIP code: {zip_code}")

        self._request_retries = request_retries
        self._session = session
        self.zip_code = zip_code

        if logger:
            self._logger = logger
        else:
            self._logger = LOGGER

        self.async_request = self._wrap_request_method(self._request_retries)

        self.allergens = Allergens(self)
        self.asthma = Asthma(self)
        self.disease = Disease(self)

    async def _async_request(
        self, method: str, url: str, **kwargs: dict[str, Any]
    ) -> dict[str, Any]:
        """Make an API request.

        Args:
            method: An HTTP method.
            url: An API URL.
            **kwargs: Additional kwargs to send with the request.

        Returns:
            An API response payload.
        """
        url_pieces = urlparse(url)
        kwargs.setdefault("headers", {})
        kwargs["headers"]["Content-Type"] = "application/json"
        kwargs["headers"]["Referer"] = f"{url_pieces.scheme}://{url_pieces.netloc}"
        kwargs["headers"]["User-Agent"] = DEFAULT_USER_AGENT

        if use_running_session := self._session and not self._session.closed:
            session = self._session
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        async with session.request(method, f"{url}/{self.zip_code}", **kwargs) as resp:
            resp.raise_for_status()
            data = await resp.json()

        if not use_running_session:
            await session.close()

        self._logger.debug("Received data for %s: %s", url, data)

        return cast(dict[str, Any], data)

    @staticmethod
    def _handle_on_giveup(_: dict[str, Any]) -> None:
        """Wrap a giveup exception as a RequestError.

        Raises:
            RequestError: Raised upon a request that has failed with multiple tries.
        """
        err_info = sys.exc_info()
        err = err_info[1].with_traceback(err_info[2])  # type: ignore[union-attr]
        raise RequestError(err) from err

    def _wrap_request_method(
        self, request_retries: int
    ) -> Callable[..., Awaitable[dict[str, Any]]]:
        """Wrap the request method in backoff/retry logic.

        Args:
            request_retries: The number of retries to give a failed request.

        Returns:
            A version of the request callable that can do retries.
        """
        return cast(
            Callable[..., Awaitable[dict[str, Any]]],
            backoff.on_exception(
                backoff.expo,
                (asyncio.TimeoutError, ClientError),
                logger=self._logger,
                max_tries=request_retries,
                on_giveup=self._handle_on_giveup,  # type: ignore[arg-type]
            )(self._async_request),
        )

    def disable_request_retries(self) -> None:
        """Disable the request retry mechanism."""
        self.async_request = self._wrap_request_method(1)

    def enable_request_retries(self) -> None:
        """Enable the request retry mechanism."""
        self.async_request = self._wrap_request_method(self._request_retries)
