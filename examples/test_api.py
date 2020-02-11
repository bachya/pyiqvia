"""Run an example script to quickly test."""
import asyncio

from aiohttp import ClientSession

from pyiqvia import Client
from pyiqvia.errors import IQVIAError


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        await run(websession)


async def run(websession):
    """Run."""
    try:
        client = Client("17015", websession)
        print(f'Client instantiated for ZIP "{client.zip_code}"')

        print()
        print("Allergen Data:")
        print(await client.allergens.current())
        print(await client.allergens.extended())
        print(await client.allergens.historic())
        print(await client.allergens.outlook())

        print()
        print("Disease Data:")
        print(await client.disease.current())
        print(await client.disease.extended())
        print(await client.disease.historic())

        print()
        print("Asthma Data:")
        print(await client.asthma.current())
        print(await client.asthma.extended())
        print(await client.asthma.historic())
    except IQVIAError as err:
        print(err)


asyncio.get_event_loop().run_until_complete(main())
