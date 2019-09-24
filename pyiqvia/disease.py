"""Define an object to work with "Disease" endpoints."""
from typing import Awaitable, Callable


class Disease:  # pylint: disable=too-few-public-methods
    """Define the "Disease" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request: Callable[..., Awaitable[dict]] = request

    async def current(self) -> dict:
        """Get current disease info."""
        return await self._request(
            "get", "https://www.flustar.com/api/forecast/current/cold"
        )

    async def extended(self) -> dict:
        """Get extended disease info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )

    async def historic(self) -> dict:
        """Get historic disease info."""
        return await self._request(
            "get", "https://www.flustar.com/api/forecast/historic/cold"
        )
