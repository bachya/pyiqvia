"""Define an object to work with allergy endpoints."""
from typing import TYPE_CHECKING, Any, Dict

if TYPE_CHECKING:
    from .client import Client


class Allergens:
    """Define the "Allergens" object."""

    def __init__(self, client: "Client") -> None:
        """Initialize."""
        self._client = client

    async def current(self) -> Dict[str, Any]:
        """Get current allergy conditions."""
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/current/pollen"
        )

    async def extended(self) -> Dict[str, Any]:
        """Get extended allergen info."""
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/extended/pollen"
        )

    async def historic(self) -> Dict[str, Any]:
        """Get historic allergen info."""
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/historic/pollen"
        )

    async def outlook(self) -> Dict[str, Any]:
        """Get allergen outlook."""
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/outlook"
        )
