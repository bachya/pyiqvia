"""Define tests for the "Allergens" object."""
import aiohttp
import pytest

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses):
    """Test getting current allergen data."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/current/pollen/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("allergens_current_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        current = await client.allergens.current()
        assert len(current["Location"]["periods"]) == 3


@pytest.mark.asyncio
async def test_extended(aresponses):
    """Test getting extended allergen info."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/extended/pollen/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("allergens_extended_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        extended = await client.allergens.extended()
        assert len(extended["Location"]["periods"]) == 5


@pytest.mark.asyncio
async def test_historic(aresponses):
    """Test getting historic allergen info."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/historic/pollen/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("allergens_historic_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        historic = await client.allergens.historic()
        assert len(historic["Location"]["periods"]) == 30


@pytest.mark.asyncio
async def test_outlook(aresponses):
    """Test getting outlook allergen info."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("allergens_outlook_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as websession:
        client = Client(TEST_ZIP, websession)
        outlook = await client.allergens.outlook()
        assert outlook["Trend"] == "subsiding"
