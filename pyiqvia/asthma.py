"""Define an object to work with asthma endpoints."""
from typing import TYPE_CHECKING, Any, Dict, cast

if TYPE_CHECKING:
    from .client import Client


class Asthma:
    """Define the "Asthma" object."""

    def __init__(self, client: "Client") -> None:
        """Initialize."""
        self._client = client

    async def current(self) -> Dict[str, Any]:
        """Get current asthma info."""
        data = await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/current/asthma"
        )
        return cast(Dict[str, Any], data)

    async def extended(self) -> Dict[str, Any]:
        """Get extended asthma info."""
        data = await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/extended/asthma"
        )
        return cast(Dict[str, Any], data)

    async def historic(self) -> Dict[str, Any]:
        """Get historic asthma info."""
        data = await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/historic/asthma"
        )
        return cast(Dict[str, Any], data)
