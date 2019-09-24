"""Define tests for the client object."""
# pylint: disable=redefined-outer-name,unused-import

import aiohttp
import pytest

from pyiqvia import Client
from pyiqvia.errors import InvalidZipError, RequestError

from .const import TEST_BAD_ZIP, TEST_ZIP


# pylint: disable=protected-access
@pytest.mark.asyncio
async def test_create():
    """Test the creation of a client."""
    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        assert client.zip_code == TEST_ZIP


@pytest.mark.asyncio
async def test_bad_zip(event_loop):
    """Test attempting to create a client with a bad ZIP code."""
    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            _ = Client(TEST_BAD_ZIP, websession)


@pytest.mark.asyncio
async def test_request_error(aresponses, event_loop):
    """Test authenticating the device."""
    aresponses.add(
        "www.pollen.com",
        f"/api/bad_endpoint/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=404),
    )
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=500),
    )

    with pytest.raises(RequestError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(TEST_ZIP, websession)
            await client._request("get", "https://www.pollen.com/api/bad_endpoint")

    with pytest.raises(RequestError):
        async with aiohttp.ClientSession(loop=event_loop) as websession:
            client = Client(TEST_ZIP, websession)
            await client.allergens.outlook()
