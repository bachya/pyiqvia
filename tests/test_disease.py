"""Define tests for the "Disease" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pyiqvia import Client

from .const import TEST_ZIP
from .fixtures.disease import *  # noqa


@pytest.mark.asyncio
async def test_current(aresponses, event_loop, fixture_current):
    """Test getting current cold and flu data."""
    aresponses.add(
        "www.flustar.com",
        f"/api/forecast/current/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_current), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        current = await client.disease.current()
        assert len(current["Location"]["periods"]) == 2


@pytest.mark.asyncio
async def test_extended(aresponses, event_loop, fixture_extended):
    """Test getting extended cold and flu data."""
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/extended/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_extended), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        extended = await client.disease.extended()
        assert len(extended["Location"]["periods"]) == 4


@pytest.mark.asyncio
async def test_historic(aresponses, event_loop, fixture_historic):
    """Test getting historic cold and flu data."""
    aresponses.add(
        "www.flustar.com",
        f"/api/forecast/historic/cold/{TEST_ZIP}",
        "get",
        aresponses.Response(text=json.dumps(fixture_historic), status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        historic = await client.disease.historic()
        assert len(historic["Location"]["periods"]) == 26
