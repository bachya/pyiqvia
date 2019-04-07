# 🌻pypyiqvia: A clean, async-focused Python3 API for IQVIA data

[![Travis CI](https://travis-ci.org/bachya/pyiqvia.svg?branch=master)](https://travis-ci.org/bachya/pyiqvia)
[![PyPi](https://img.shields.io/pypi/v/pyiqvia.svg)](https://pypi.python.org/pypi/pyiqvia)
[![Version](https://img.shields.io/pypi/pyversions/pyiqvia.svg)](https://pypi.python.org/pypi/pyiqvia)
[![License](https://img.shields.io/pypi/l/pyiqvia.svg)](https://github.com/bachya/pyiqvia/blob/master/LICENSE)
[![Code Coverage](https://codecov.io/gh/bachya/pyiqvia/branch/master/graph/badge.svg)](https://codecov.io/gh/bachya/pyiqvia)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8bab14f84196490b4a7/maintainability)](https://codeclimate.com/github/bachya/pyiqvia/maintainability)
[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)

`pyiqvia` is an async-focused Python3 library for allergen, asthma, and disease data
from the [IQVIA](https://www.iqvia.com) family of websites (such as 
https://pollen.com, https://flustar.com, and more).

# Python Versions

`pyiqvia` is currently supported on:

* Python 3.5
* Python 3.6
* Python 3.7

However, running the test suite currently requires Python 3.6 or higher; tests
run on Python 3.5 will fail.

# Installation

```python
pip install pyiqvia
```

# Usage

`pyiqvia` starts within an
[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:

```python
import asyncio

from aiohttp import ClientSession

from pyiqvia import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      # YOUR CODE HERE


asyncio.get_event_loop().run_until_complete(main())
```

Create a client and get to it:

```python
import asyncio

from aiohttp import ClientSession

from pyiqvia import Client


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
      client = Client(80012, websession)

      # ZIP codes starting with 0 need to be provided as strings:
      client = Client('00544', websession)

      # Get current allergen information:
      await client.allergens.current()

      # Get more information on the current allergen outlook:
      await client.allergens.outlook()

      # Get extended forecast allergen information:
      await client.allergens.extended()

      # Get historic allergen information:
      await client.allergens.historic()

      # Get current asthma information:
      await client.asthma.current()

      # Get extended forecast asthma information:
      await client.asthma.extended()

      # Get historic asthma information:
      await client.asthma.historic()

      # Get extended forecast cold and flu information:
      await client.disease.extended()


asyncio.get_event_loop().run_until_complete(main())
```

# Contributing

1. [Check for open features/bugs](https://github.com/bachya/pyiqvia/issues)
  or [initiate a discussion on one](https://github.com/bachya/pyiqvia/issues/new).
2. [Fork the repository](https://github.com/bachya/pyiqvia/fork).
3. Install the dev environment: `make init`.
4. Enter the virtual environment: `pipenv shell`
5. Code your new feature or bug fix.
6. Write a test that covers your new functionality.
7. Run tests and ensure 100% code coverage: `make coverage`
8. Add yourself to `AUTHORS.md`.
9. Submit a pull request!
