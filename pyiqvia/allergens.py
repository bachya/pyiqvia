"""Define an object to work with "Allergens" endpoints."""
from typing import Awaitable, Callable


class Allergens:
    """Define the "Allergens" object."""

    def __init__(self, request: Callable[..., Awaitable[dict]]) -> None:
        """Initialize."""
        self._request: Callable[..., Awaitable[dict]] = request

    async def current(self) -> dict:
        """Get current allergy conditions."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/current/pollen"
        )

    async def extended(self) -> dict:
        """Get extended allergen info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/extended/pollen"
        )

    async def historic(self) -> dict:
        """Get historic allergen info."""
        return await self._request(
            "get", "https://www.pollen.com/api/forecast/historic/pollen"
        )

    async def outlook(self) -> dict:
        """Get allergen outlook."""
        return await self._request("get", "https://www.pollen.com/api/forecast/outlook")
