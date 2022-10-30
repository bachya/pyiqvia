"""Define tests for the "Allergens" object."""
from __future__ import annotations

import json

import aiohttp
import pytest
from aresponses import ResponsesMockServer

from pyiqvia import Client

from .common import TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_current(aresponses: ResponsesMockServer) -> None:
    """Test getting current allergen data.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/current/pollen/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_current_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        current = await client.allergens.current()
        assert len(current["Location"]["periods"]) == 3

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_current_no_explicit_session(aresponses: ResponsesMockServer) -> None:
    """Test getting current allergen data without an explicit aiohttp ClientSession.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/current/pollen/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_current_response.json")), status=200
        ),
    )

    client = Client(TEST_ZIP)
    current = await client.allergens.current()
    assert len(current["Location"]["periods"]) == 3

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_extended(aresponses: ResponsesMockServer) -> None:
    """Test getting extended allergen info.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/extended/pollen/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_extended_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        extended = await client.allergens.extended()
        assert len(extended["Location"]["periods"]) == 5

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_historic(aresponses: ResponsesMockServer) -> None:
    """Test getting historic allergen info.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/historic/pollen/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_historic_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        historic = await client.allergens.historic()
        assert len(historic["Location"]["periods"]) == 30

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_outlook(aresponses: ResponsesMockServer) -> None:
    """Test getting outlook allergen info.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_outlook_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        outlook = await client.allergens.outlook()
        assert outlook["Trend"] == "subsiding"

    aresponses.assert_plan_strictly_followed()
