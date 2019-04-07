"""Define errors."""


class IQVIAError(Exception):
    """Define a base package error."""


class InvalidZipError(IQVIAError):
    """Define an error when a ZIP returns no valid data."""


class RequestError(IQVIAError):
    """Define a generic request error."""
