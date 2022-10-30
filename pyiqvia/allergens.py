"""Define an object to work with allergy endpoints."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .client import Client


class Allergens:
    """Define the "Allergens" object."""

    def __init__(self, client: Client) -> None:
        """Initialize.

        Args:
            client: The Client object.
        """
        self._client = client

    async def current(self) -> dict[str, Any]:
        """Get current allergy conditions.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/current/pollen"
        )

    async def extended(self) -> dict[str, Any]:
        """Get extended allergen info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/extended/pollen"
        )

    async def historic(self) -> dict[str, Any]:
        """Get historic allergen info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/historic/pollen"
        )

    async def outlook(self) -> dict[str, Any]:
        """Get allergen outlook.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/outlook"
        )
