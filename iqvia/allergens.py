"""Define an object to work with "Allergens" endpoints."""
from typing import Awaitable, Callable

from .decorators import raise_on_invalid_zip
from .errors import InvalidZipError, RequestError


class Allergens:
    """Define the "Allergens" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request = request

    @raise_on_invalid_zip
    async def current(self) -> dict:
        """Get current allergy conditions."""
        return await self._request(
            'get', 'https://www.pollen.com/api/forecast/current/pollen')

    @raise_on_invalid_zip
    async def extended(self) -> dict:
        """Get extended allergen info."""
        return await self._request(
            'get', 'https://www.pollen.com/api/forecast/extended/pollen')

    @raise_on_invalid_zip
    async def historic(self) -> dict:
        """Get historic allergen info."""
        return await self._request(
            'get', 'https://www.pollen.com/api/forecast/historic/pollen')

    async def outlook(self) -> dict:
        """Get allergen outlook."""
        try:
            return await self._request(
                'get', 'https://www.pollen.com/api/forecast/outlook')
        except RequestError as err:
            if '404' in str(err):
                raise InvalidZipError('No data returned for ZIP code')
            else:
                raise RequestError(err)
