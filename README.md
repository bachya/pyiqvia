# 🌻 pyiqvia: A clean, async-focused Python3 API for IQVIA™

[![CI][ci-badge]][ci]
[![PyPI][pypi-badge]][pypi]
[![Version][version-badge]][version]
[![License][license-badge]][license]
[![Code Coverage][codecov-badge]][codecov]
[![Maintainability][maintainability-badge]][maintainability]

<a href="https://www.buymeacoffee.com/bachya1208P" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

`pyiqvia` is an async-focused Python3 library for allergen, asthma, and disease data from
the [IQVIA™][iqvia] family of websites (such as [Pollen.com][pollen],
[FluStar][flustar], and more).

- [Python Versions](#python-versions)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

# Python Versions

`pyiqvia` is currently supported on:

- Python 3.10
- Python 3.11
- Python 3.12

# Installation

```bash
pip install pyiqvia
```

# Usage

```python
import asyncio

from aiohttp import ClientSession

from pyiqvia import Client


async def main() -> None:
    """Run!"""
    # Note that ZIP codes must be provided as strings:
    client = Client("80012")

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

    # Get current cold and flu information:
    await client.disease.current()

    # Get extended forecast cold and flu information:
    await client.disease.extended()

    # Get historic cold and flu information:
    await client.disease.historic()


asyncio.run(main())
```

## Retries

By default, `pyiqvia` will retry appropriate errors 4 times (with an exponentially
increasing delay in-between). This logic can be changed by passing a different value for
`request_retries` to the `Client` constructor:

```python
import asyncio

from pyiqvia import Client


async def main():
    client = Client("80012", request_retries=5)

    # ...


asyncio.run(main())
```

## Connection Pooling

By default, the library creates a new connection to IQVIA with each coroutine. If you
are calling a large number of coroutines (or merely want to squeeze out every second of
runtime savings possible), an [`aiohttp`][aiohttp] `ClientSession` can be used for
connection pooling:

```python
import asyncio

from aiohttp import ClientSession

from pyiqvia import Client


async def main() -> None:
    """Run!"""
    async with ClientSession() as session:
        client = Client("80012", session=session)

        # ...


asyncio.run(main())
```

# Contributing

Thanks to all of [our contributors][contributors] so far!

1. [Check for open features/bugs][issues] or [initiate a discussion on one][new-issue].
2. [Fork the repository][fork].
3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`
4. (_optional, but highly recommended_) Enter the virtual environment: `source ./.venv/bin/activate`
5. Install the dev environment: `script/setup`
6. Code your new feature or bug fix on a new branch.
7. Write tests that cover your new functionality.
8. Run tests and ensure 100% code coverage: `poetry run pytest --cov pyiqvia tests`
9. Update `README.md` with any new documentation.
10. Submit a pull request!

[aiohttp]: https://github.com/aio-libs/aiohttp
[ci-badge]: https://github.com/bachya/pyiqvia/workflows/CI/badge.svg
[ci]: https://github.com/bachya/pyiqvia/actions
[codecov-badge]: https://codecov.io/gh/bachya/pyiqvia/branch/dev/graph/badge.svg
[codecov]: https://codecov.io/gh/bachya/pyiqvia
[contributors]: https://github.com/bachya/pyiqvia/graphs/contributors
[flustar]: https://flustar.com
[fork]: https://github.com/bachya/pyiqvia/fork
[iqvia]: https://www.iqvia.com
[issues]: https://github.com/bachya/pyiqvia/issues
[license-badge]: https://img.shields.io/pypi/l/pyiqvia.svg
[license]: https://github.com/bachya/pyiqvia/blob/main/LICENSE
[maintainability-badge]: https://api.codeclimate.com/v1/badges/3bf37f9cabf73b5d991e/maintainability
[maintainability]: https://codeclimate.com/github/bachya/pyiqvia/maintainability
[new-issue]: https://github.com/bachya/pyiqvia/issues/new
[new-issue]: https://github.com/bachya/pyiqvia/issues/new
[pollen]: https://pollen.com
[pypi-badge]: https://img.shields.io/pypi/v/pyiqvia.svg
[pypi]: https://pypi.python.org/pypi/pyiqvia
[version-badge]: https://img.shields.io/pypi/pyversions/pyiqvia.svg
[version]: https://pypi.python.org/pypi/pyiqvia
