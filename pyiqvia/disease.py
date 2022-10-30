"""Define an object to work with disease endpoints."""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .client import Client


class Disease:
    """Define the "Disease" object."""

    def __init__(self, client: Client) -> None:
        """Initialize.

        Args:
            client: The Client object.
        """
        self._client = client

    async def current(self) -> dict[str, Any]:
        """Get current disease info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://flustar.com/api/forecast/current/cold"
        )

    async def extended(self) -> dict[str, Any]:
        """Get extended disease info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://www.pollen.com/api/forecast/extended/cold"
        )

    async def historic(self) -> dict[str, Any]:
        """Get historic disease info.

        Returns:
            An API response payload.
        """
        return await self._client.async_request(
            "get", "https://flustar.com/api/forecast/historic/cold"
        )
