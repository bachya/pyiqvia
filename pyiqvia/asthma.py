"""Define an object to work with asthma endpoints."""
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from .client import Client


class Asthma:
    """Define the "Asthma" object."""

    def __init__(self, client: "Client") -> None:
        """Initialize."""
        self._client = client

    async def current(self) -> Dict[str, Any]:
        """Get current asthma info."""
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/current/asthma"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended asthma info."""
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/extended/asthma"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic asthma info."""
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/historic/asthma"
        )
