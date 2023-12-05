#!/usr/bin/python3

""" A module that returns JSON representation of a string
"""


import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)
    Args:
        my_obj: object to be serialized
    Return the JSON representation
    """
    return json.dumps(my_obj)
