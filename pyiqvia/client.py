"""Define a client to interact with Pollen.com."""
from urllib.parse import urlparse

from aiohttp import ClientSession, client_exceptions

from .allergens import Allergens
from .asthma import Asthma
from .disease import Disease
from .errors import RequestError

API_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) ' \
    + 'AppleWebKit/537.36 (KHTML, like Gecko) ' \
    + 'Chrome/65.0.3325.181 Safari/537.36'


class Client:  # pylint: disable=too-few-public-methods
    """Define the client."""

    def __init__(self, zip_code: str, websession: ClientSession) -> None:
        """Initialize."""
        self._websession = websession
        self.zip_code = zip_code

        self.allergens = Allergens(self._request)
        self.asthma = Asthma(self._request)
        self.disease = Disease(self._request)

    async def _request(
            self,
            method: str,
            url: str,
            *,
            headers: dict = None,
            params: dict = None,
            json: dict = None) -> dict:
        """Make a request against AirVisual."""
        full_url = '{0}/{1}'.format(url, self.zip_code)
        pieces = urlparse(url)

        if not headers:
            headers = {}
        headers.update({
            'Content-Type': 'application/json',
            'Referer': '{0}://{1}'.format(pieces.scheme, pieces.netloc),
            'User-Agent': API_USER_AGENT
        })

        async with self._websession.request(method, full_url, headers=headers,
                                            params=params, json=json) as resp:
            try:
                resp.raise_for_status()
                data = await resp.json(content_type=None)
                return data
            except client_exceptions.ClientError as err:
                raise RequestError(
                    'Error requesting data from {0}: {1}'.format(url, err))
