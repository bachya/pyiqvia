"""Define errors."""


class PollenComError(Exception):
    """Define a base package error."""


class InvalidZipError(PollenComError):
    """Define an error when a ZIP returns no valid data."""


class RequestError(PollenComError):
    """Define a generic request error."""
