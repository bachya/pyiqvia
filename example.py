"""Run an example script to quickly test."""
import asyncio

from aiohttp import ClientSession

from pypollencom import Client
from pypollencom.errors import PollenComError


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        await run(websession)


async def run(websession):
    """Run."""
    try:
        client = Client('17015', websession)
        print('Client instantiated for ZIP "{0}"'.format(client.zip_code))

        print()
        print('CURRENT ALLERGENS')
        print(await client.allergens.current())

        print()
        print('EXTENDED ALLERGENS')
        print(await client.allergens.extended())

        print()
        print('HISTORIC ALLERGENS')
        print(await client.allergens.historic())

        print()
        print('ALLERGY OUTLOOK')
        print(await client.allergens.outlook())

        print()
        print('EXTENDED DISEASE INFO')
        print(await client.disease.extended())

        print()
        print('CURRENT ASTHMA INFO')
        print(await client.asthma.current())

        print()
        print('EXTENDED ASTHMA INFO')
        print(await client.asthma.extended())

        print()
        print('HISTORIC ASTHMA INFO')
        print(await client.asthma.historic())
    except PollenComError as err:
        print(err)


asyncio.get_event_loop().run_until_complete(main())
