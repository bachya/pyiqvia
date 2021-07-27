"""Define an object to work with "Disease" endpoints."""
from typing import Any, Awaitable, Callable, Dict


class Disease:  # pylint: disable=too-few-public-methods
    """Define the "Disease" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request = request

    async def current(self) -> Dict[str, Any]:
        """Get current disease info."""
        return await self._request(
            "get", "https://flustar.com/api/forecast/current/cold"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended disease info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic disease info."""
        return await self._request(
            "get", "https://flustar.com/api/forecast/historic/cold"
        )
