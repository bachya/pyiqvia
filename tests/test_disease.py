"""Define tests for the "Disease" object."""
# pylint: disable=redefined-outer-name,unused-import

import json

import aiohttp
import pytest

from pyiqvia import Client

from .const import TEST_ZIP
from .fixtures.disease import *  # noqa


@pytest.mark.asyncio
async def test_endpoints(
        aresponses, event_loop, fixture_current, fixture_extended,
        fixture_historic):
    """Test all endpoints."""
    aresponses.add(
        'www.flustar.com',
        '/api/forecast/current/cold/{0}'.format(TEST_ZIP), 'get',
        aresponses.Response(text=json.dumps(fixture_current), status=200))
    aresponses.add(
        'www.pollen.com', '/api/forecast/extended/cold/{0}'.format(TEST_ZIP),
        'get',
        aresponses.Response(text=json.dumps(fixture_extended), status=200))
    aresponses.add(
        'www.flustar.com', '/api/forecast/historic/cold/{0}'.format(TEST_ZIP),
        'get',
        aresponses.Response(text=json.dumps(fixture_historic), status=200))

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        client = Client(TEST_ZIP, websession)

        current = await client.disease.current()
        assert len(current['Location']['periods']) == 2

        extended = await client.disease.extended()
        assert len(extended['Location']['periods']) == 4

        historic = await client.disease.historic()
        assert len(historic['Location']['periods']) == 26
