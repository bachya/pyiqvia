"""Define a client to interact with Pollen.com."""
from typing import Optional
from urllib.parse import ParseResult, urlparse

from aiohttp import ClientSession, client_exceptions

from .allergens import Allergens
from .asthma import Asthma
from .disease import Disease
from .errors import InvalidZipError, RequestError

API_USER_AGENT: str = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) "
    + "AppleWebKit/537.36 (KHTML, like Gecko) "
    + "Chrome/65.0.3325.181 Safari/537.36"
)


def is_valid_zip_code(zip_code: str) -> bool:
    """Define whether a string ZIP code is valid."""
    return len(zip_code) == 5 and zip_code.isdigit()


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(self, zip_code: str, websession: ClientSession) -> None:
        """Initialize."""
        if not is_valid_zip_code(zip_code):
            raise InvalidZipError(f"Invalid ZIP code: {zip_code}")

        self._websession: ClientSession = websession
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

        if not headers:
            headers = {}
        headers.update(
            {
                "Content-Type": "application/json",
                "Referer": f"{pieces.scheme}://{pieces.netloc}",
                "User-Agent": API_USER_AGENT,
            }
        )

        async with self._websession.request(
            method, f"{url}/{self.zip_code}", headers=headers, params=params, json=json
        ) as resp:
            try:
                resp.raise_for_status()
                data: dict = await resp.json(content_type=None)
                return data
            except client_exceptions.ClientError as err:
                raise RequestError(f"Error requesting data from {url}: {err}")
