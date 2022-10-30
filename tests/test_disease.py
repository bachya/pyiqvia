"""Define tests for the "Disease" object."""
from __future__ import annotations

import json

import aiohttp
import pytest
from aresponses import ResponsesMockServer

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses: ResponsesMockServer) -> None:
    """Test getting current cold and flu data.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "flustar.com",
        f"/api/forecast/current/cold/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("disease_current_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        current = await client.disease.current()
        assert len(current["Location"]["periods"]) == 2

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_extended(aresponses: ResponsesMockServer) -> None:
    """Test getting extended cold and flu data.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/extended/cold/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("disease_extended_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        extended = await client.disease.extended()
        assert len(extended["Location"]["periods"]) == 4

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_historic(aresponses: ResponsesMockServer) -> None:
    """Test getting historic cold and flu data.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "flustar.com",
        f"/api/forecast/historic/cold/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("disease_historic_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        historic = await client.disease.historic()
        assert len(historic["Location"]["periods"]) == 26

    aresponses.assert_plan_strictly_followed()
