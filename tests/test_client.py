"""Define tests for the client object."""
from __future__ import annotations

import asyncio
import json
import logging
from unittest.mock import Mock, patch

import aiohttp
import pytest
from aresponses import ResponsesMockServer

from pyiqvia import Client
from pyiqvia.errors import InvalidZipError, RequestError

from .common import TEST_BAD_ZIP, TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_bad_zip() -> None:
    """Test creating a client with a bad ZIP code."""
    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession() as session:
            _ = Client(TEST_BAD_ZIP, session=session)


@pytest.mark.asyncio
async def test_create() -> None:
    """Test the creation of a client."""
    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        assert client.zip_code == TEST_ZIP


@pytest.mark.asyncio
async def test_custom_logger(aresponses: ResponsesMockServer, caplog: Mock) -> None:
    """Test that a custom logger is used when provided to the client.

    Args:
        aresponses: An aresponses server.                            :
        caplog: A mock logging utility.
    """
    caplog.set_level(logging.DEBUG)
    custom_logger = logging.getLogger("custom")

    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/current/pollen/{TEST_ZIP}",
        "get",
        response=aiohttp.web_response.json_response(
            json.loads(load_fixture("allergens_current_response.json")), status=200
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session, logger=custom_logger)
        await client.allergens.current()
        assert any(
            record.name == "custom" and "Received data" in record.message
            for record in caplog.records
        )

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_http_error(aresponses: ResponsesMockServer) -> None:
    """Test an HTTP error.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=500),
    )

    with pytest.raises(RequestError):
        async with aiohttp.ClientSession() as session:
            client = Client(TEST_ZIP, session=session, request_retries=1)
            await client.allergens.outlook()

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_request_retries(aresponses: ResponsesMockServer) -> None:
    """Test the request retry logic.

    Args:
        aresponses: An aresponses server.
    """
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=500),
    )
    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/outlook/{TEST_ZIP}",
        "get",
        aresponses.Response(text="", status=500),
    )
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

        client.disable_request_retries()

        with pytest.raises(RequestError):
            await client.allergens.outlook()

        client.enable_request_retries()

        await client.allergens.outlook()

    aresponses.assert_plan_strictly_followed()


@pytest.mark.asyncio
async def test_request_timeout() -> None:
    """Test a request timeout."""
    with patch(
        "aiohttp.ClientSession.request", side_effect=asyncio.TimeoutError
    ), pytest.raises(RequestError):
        async with aiohttp.ClientSession() as session:
            client = Client(TEST_ZIP, session=session, request_retries=1)
            await client.allergens.outlook()
