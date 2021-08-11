"""Define an object to work with disease endpoints."""
from typing import Any, Awaitable, Callable, Dict


class Disease:
    """Define the "Disease" object."""

    def __init__(self, async_request: Callable[..., Awaitable[Dict[str, Any]]]) -> None:
        """Initialize."""
        self._async_request = async_request

    async def current(self) -> Dict[str, Any]:
        """Get current disease info."""
        return await self._async_request(
            "get", "https://flustar.com/api/forecast/current/cold"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended disease info."""
        return await self._async_request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic disease info."""
        return await self._async_request(
            "get", "https://flustar.com/api/forecast/historic/cold"
        )
