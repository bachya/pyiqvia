"""Define useful decorators."""
from typing import Callable

from .errors import InvalidZipError


def raise_on_invalid_zip(func: Callable) -> Callable:
    """Raise an exception when there's no data (via a bad ZIP code)."""
    async def decorator(*args: list, **kwargs: dict) -> dict:
        """Decorate."""
        data = await func(*args, **kwargs)
        if not data['Location']['periods']:
            raise InvalidZipError('No data returned for ZIP code')
        return data

    return decorator
