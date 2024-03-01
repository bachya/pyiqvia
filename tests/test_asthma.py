"""Define tests for the "Asthma" object."""

from __future__ import annotations

import json

import aiohttp
import pytest
from aresponses import ResponsesMockServer

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses: ResponsesMockServer) -> None:
    """Test getting current asthma.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/current/asthma/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("asthma_current_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        current = await client.asthma.current()
        assert len(current["Location"]["periods"]) == 3

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_extended(aresponses: ResponsesMockServer) -> None:
    """Test getting extended asthma info.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/extended/asthma/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("asthma_extended_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        extended = await client.asthma.extended()
        assert len(extended["Location"]["periods"]) == 5

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_endpoints(aresponses: ResponsesMockServer) -> None:
    """Test getting historic asthma info.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.asthmaforecast.com",
        f"/api/forecast/historic/asthma/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("asthma_historic_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        historic = await client.asthma.historic()
        assert len(historic["Location"]["periods"]) == 30

    aresponses.assert_plan_strictly_followed()
