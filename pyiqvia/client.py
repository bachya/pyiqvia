"""Define a client to interact with Pollen.com."""
from typing import Optional
from urllib.parse import ParseResult, urlparse

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError

from .allergens import Allergens
from .asthma import Asthma
from .disease import Disease
from .errors import InvalidZipError, RequestError

DEFAULT_TIMEOUT: int = 10
DEFAULT_USER_AGENT: str = (
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
        self, zip_code: str, *, session: Optional[ClientSession] = None
    ) -> None:
        """Initialize."""
        if not is_valid_zip_code(zip_code):
            raise InvalidZipError(f"Invalid ZIP code: {zip_code}")

        self._session: ClientSession = session
        self.zip_code: str = zip_code

        self.allergens: Allergens = Allergens(self._request)
        self.asthma: Asthma = Asthma(self._request)
        self.disease: Disease = Disease(self._request)

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
        pieces: ParseResult = urlparse(url)

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
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        try:
            async with session.request(
                method,
                f"{url}/{self.zip_code}",
                headers=_headers,
                params=params,
                json=json,
            ) as resp:
                resp.raise_for_status()
                data: dict = await resp.json(content_type=None)
                return data
        except ClientError as err:
            raise RequestError(f"Error requesting data from {url}: {err}")
        finally:
            if not use_running_session:
                await session.close()
