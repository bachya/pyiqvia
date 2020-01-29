"""Define tests for the client object."""
import aiohttp
import pytest

from pyiqvia import Client
from pyiqvia.errors import InvalidZipError, RequestError

from .common import TEST_BAD_ZIP, TEST_ZIP


@pytest.mark.asyncio
async def test_create():
    """Test the creation of a client."""
    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        assert client.zip_code == TEST_ZIP


@pytest.mark.asyncio
async def test_bad_zip():
    """Test attempting to create a client with a bad ZIP code."""
    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession() as websession:
            _ = Client(TEST_BAD_ZIP, websession)


@pytest.mark.asyncio
async def test_request_error(aresponses):
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
        async with aiohttp.ClientSession() as websession:
            client = Client(TEST_ZIP, websession)
            await client._request("get", "https://www.pollen.com/api/bad_endpoint")
            await client.allergens.outlook()
