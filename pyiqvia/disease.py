"""Define an object to work with disease endpoints."""
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from .client import Client


class Disease:
    """Define the "Disease" object."""

    def __init__(self, client: "Client") -> None:
        """Initialize."""
        self._client = client

    async def current(self) -> Dict[str, Any]:
        """Get current disease info."""
        return await self._client.async_request(
            "get", "https://flustar.com/api/forecast/current/cold"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended disease info."""
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic disease info."""
        return await self._client.async_request(
            "get", "https://flustar.com/api/forecast/historic/cold"
        )
