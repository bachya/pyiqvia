"""Define an object to work with disease endpoints."""
from typing import TYPE_CHECKING, Any, Dict, cast

if TYPE_CHECKING:
    from .client import Client


class Disease:
    """Define the "Disease" object."""

    def __init__(self, client: "Client") -> None:
        """Initialize."""
        self._client = client

    async def current(self) -> Dict[str, Any]:
        """Get current disease info."""
        data = await self._client.async_request(
            "get", "https://flustar.com/api/forecast/current/cold"
        )
        return cast(Dict[str, Any], data)

    async def extended(self) -> Dict[str, Any]:
        """Get extended disease info."""
        data = await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )
        return cast(Dict[str, Any], data)

    async def historic(self) -> Dict[str, Any]:
        """Get historic disease info."""
        data = await self._client.async_request(
            "get", "https://flustar.com/api/forecast/historic/cold"
        )
        return cast(Dict[str, Any], data)
