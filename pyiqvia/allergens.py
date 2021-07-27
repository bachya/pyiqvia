"""Define an object to work with "Allergens" endpoints."""
from typing import Any, Awaitable, Callable, Dict


class Allergens:
    """Define the "Allergens" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request = request

    async def current(self) -> Dict[str, Any]:
        """Get current allergy conditions."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/current/pollen"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended allergen info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/extended/pollen"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic allergen info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/historic/pollen"
        )

    async def outlook(self) -> Dict[str, Any]:
        """Get allergen outlook."""
        return await self._request("get", "https://www.pollen.com/api/forecast/outlook")
