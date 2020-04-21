"""Define tests for the "Asthma" object."""
import aiohttp
import pytest

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses):
    """Test getting current asthma."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/current/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("asthma_current_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        current = await client.asthma.current()
        assert len(current["Location"]["periods"]) == 3


@pytest.mark.asyncio
async def test_extended(aresponses):
    """Test getting extended asthma info."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/extended/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("asthma_extended_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        extended = await client.asthma.extended()
        assert len(extended["Location"]["periods"]) == 5


@pytest.mark.asyncio
async def test_endpoints(aresponses):
    """Test getting historic asthma info."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/historic/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("asthma_historic_response.json"), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        historic = await client.asthma.historic()
        assert len(historic["Location"]["periods"]) == 30
