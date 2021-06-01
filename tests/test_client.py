"""Define tests for the client object."""
import aiohttp
import pytest

from pyiqvia import Client
from pyiqvia.errors import InvalidZipError, RequestError

from .common import TEST_BAD_ZIP, TEST_ZIP


@pytest.mark.asyncio
async def test_bad_zip():
    """Test creating a client with a bad ZIP code."""
    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession() as session:
            _ = Client(TEST_BAD_ZIP, session=session)


@pytest.mark.asyncio
async def test_create():
    """Test the creation of a client."""
    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        assert client.zip_code == TEST_ZIP


@pytest.mark.asyncio
async def test_http_error(aresponses):
    """Test that an HTTP error throws an exception."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=500),
    )

    with pytest.raises(RequestError):
        async with aiohttp.ClientSession() as session:
            client = Client(TEST_ZIP, session=session)
            await client.allergens.outlook()
