"""Define an object to work with asthma endpoints."""
from typing import Any, Awaitable, Callable, Dict


class Asthma:
    """Define the "Asthma" object."""

    def __init__(self, async_request: Callable[..., Awaitable[Dict[str, Any]]]) -> None:
        """Initialize."""
        self._async_request = async_request

    async def current(self) -> Dict[str, Any]:
        """Get current asthma info."""
        return await self._async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/current/asthma"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended asthma info."""
        return await self._async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/extended/asthma"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic asthma info."""
        return await self._async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/historic/asthma"
        )
