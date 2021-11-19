"""Define tests for the client object."""
import asyncio
import logging
from unittest.mock import patch

import aiohttp
import pytest

from pyiqvia import Client
from pyiqvia.errors import InvalidZipError, RequestError

from .common import TEST_BAD_ZIP, TEST_ZIP, load_fixture


@pytest.mark.asyncio
async def test_bad_zip():
    """Test creating a client with a bad ZIP code."""
    with pytest.raises(InvalidZipError):
        async with aiohttp.ClientSession() as session:
            _ = Client(TEST_BAD_ZIP, session=session)


@pytest.mark.asyncio
async def test_create():
    """Test the creation of a client."""
    async with aiohttp.ClientSession() as session:
        client = Client(TEST_ZIP, session=session)
        assert client.zip_code == TEST_ZIP


@pytest.mark.asyncio
async def test_custom_logger(aresponses, caplog):
    """Test that a custom logger is used when provided to the client."""
    caplog.set_level(logging.DEBUG)
    custom_logger = logging.getLogger("custom")

    aresponses.add(
        "www.pollen.com",
        f"/api/forecast/current/pollen/{TEST_ZIP}",
        "get",
        aresponses.Response(
            text=load_fixture("allergens_current_response.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
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
async def test_http_error(aresponses):
    """Test an HTTP error."""
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
async def test_request_timeout():
    """Test a request timeout."""
    with patch(
        "aiohttp.ClientSession.request", side_effect=asyncio.exceptions.TimeoutError
    ), pytest.raises(RequestError):
        async with aiohttp.ClientSession() as session:
            client = Client(TEST_ZIP, session=session, request_retries=1)
            await client.allergens.outlook()


@pytest.mark.asyncio
async def test_request_retries(aresponses):
    """Test the request retry logic."""
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
        aresponses.Response(
            text=load_fixture("allergens_outlook_response.json"),
            status=200,
            headers={"Content-Type": "application/json; charset=utf-8"},
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
