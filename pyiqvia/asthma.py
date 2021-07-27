"""Define an object to work with "Ashtma" endpoints."""
from typing import Any, Awaitable, Callable, Dict


class Asthma:  # pylint: disable=too-few-public-methods
    """Define the "Asthma" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request = request

    async def current(self) -> Dict[str, Any]:
        """Get current asthma info."""
        return await self._request(
            "get", "https://www.asthmaforecast.com/api/forecast/current/asthma"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended asthma info."""
        return await self._request(
            "get", "https://www.asthmaforecast.com/api/forecast/extended/asthma"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic asthma info."""
        return await self._request(
            "get", "https://www.asthmaforecast.com/api/forecast/historic/asthma"
        )
