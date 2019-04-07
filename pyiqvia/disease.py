"""Define an object to work with "Disease" endpoints."""
from typing import Awaitable, Callable

from .decorators import raise_on_invalid_zip


class Disease:  # pylint: disable=too-few-public-methods
    """Define the "Disease" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request = request

    @raise_on_invalid_zip
    async def current(self) -> dict:
        """Get current disease info."""
        return await self._request(
            'get', 'https://www.flustar.com/api/forecast/current/cold')

    @raise_on_invalid_zip
    async def extended(self) -> dict:
        """Get extended disease info."""
        return await self._request(
            'get', 'https://www.pollen.com/api/forecast/extended/cold')

    @raise_on_invalid_zip
    async def historic(self) -> dict:
        """Get historic disease info."""
        return await self._request(
            'get', 'https://www.flustar.com/api/forecast/historic/cold')
