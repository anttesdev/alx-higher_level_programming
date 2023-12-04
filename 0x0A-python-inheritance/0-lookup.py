#!/usr/bin/python3

""" Defines a look up function with an object argument"""


def lookup(obj):
    """ A function that returns the list of available
    attributes and methods of an object
    """

    List = dir(obj)
    return List
