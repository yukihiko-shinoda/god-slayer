"""This module implements exceptions for this package."""

__all__ = ["Error", "InvalidRecordError", "InvalidHeaderError", "InvalidFooterError", "LogicError"]


class Error(Exception):
    """
    Base class for exceptions in this module.
    @see https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """


class InvalidRecordError(Error):
    """Target record is invalid."""


class InvalidHeaderError(InvalidRecordError):
    """Header record is invalid."""


class InvalidFooterError(InvalidRecordError):
    """Footer record is invalid."""


class LogicError(Error):
    """This Error indicates programing miss."""
