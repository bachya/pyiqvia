"""Define an object to work with asthma endpoints."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .client import Client


class Asthma:
    """Define the "Asthma" object."""

    def __init__(self, client: Client) -> None:
        """Initialize.

        Args:
            client: The Client object.
        """
        self._client = client

    async def current(self) -> dict[str, Any]:
        """Get current asthma info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/current/asthma"
        )

    async def extended(self) -> dict[str, Any]:
        """Get extended asthma info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/extended/asthma"
        )

    async def historic(self) -> dict[str, Any]:
        """Get historic asthma info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.asthmaforecast.com/api/forecast/historic/asthma"
        )
