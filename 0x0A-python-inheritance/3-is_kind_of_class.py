#!/usr/bin/python3
"""A function that checks if an object is an instance of, or
    inherited from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of,
        or inherited from, the specified class."""
    return isinstance(obj, a_class)
