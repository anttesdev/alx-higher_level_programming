#!/usr/bin/python3
""" creates a locked class"""


class LockedClass:
    """
    defines a locked class that will have instantiation of an
    attribute named first name, but doesnt for anything else
    """

    __slots__ = ["first_name"]
