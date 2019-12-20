"""Define tests for the "Asthma" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pyiqvia import Client

from .const import TEST_ZIP
from .fixtures.asthma import *  # noqa


@pytest.mark.asyncio
async def test_current(aresponses, event_loop, fixture_current):
    """Test getting current asthma."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/current/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_current), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        current = await client.asthma.current()
        assert len(current["Location"]["periods"]) == 3


@pytest.mark.asyncio
async def test_extended(aresponses, event_loop, fixture_extended):
    """Test getting extended asthma info."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/extended/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_extended), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        extended = await client.asthma.extended()
        assert len(extended["Location"]["periods"]) == 5


@pytest.mark.asyncio
async def test_endpoints(aresponses, event_loop, fixture_historic):
    """Test getting historic asthma info."""
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/historic/asthma/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_historic), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        historic = await client.asthma.historic()
        assert len(historic["Location"]["periods"]) == 30
