#!/usr/bin/python3
"""
A module that deserializes a string
"""


import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str: string to be deserialized
    Return the serialized object
    """
    return json.load(my_str)
