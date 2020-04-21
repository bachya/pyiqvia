"""Define tests for the "Disease" object."""
import aiohttp
import pytest

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses):
    """Test getting current cold and flu data."""
    aresponses.add(
        "www.flustar.com",
        f"/api/forecast/current/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("disease_current_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        current = await client.disease.current()
        assert len(current["Location"]["periods"]) == 2


@pytest.mark.asyncio
async def test_extended(aresponses):
    """Test getting extended cold and flu data."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/extended/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("disease_extended_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        extended = await client.disease.extended()
        assert len(extended["Location"]["periods"]) == 4


@pytest.mark.asyncio
async def test_historic(aresponses):
    """Test getting historic cold and flu data."""
    aresponses.add(
        "www.flustar.com",
        f"/api/forecast/historic/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("disease_historic_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        historic = await client.disease.historic()
        assert len(historic["Location"]["periods"]) == 26
