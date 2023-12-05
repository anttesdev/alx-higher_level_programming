#!/usr/bin/python3
"""
A module to create an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”
    Args:
        filename: the file name
    Return the object file
    """
    with open(filename, 'r', encoding='utf-8') as new:
        return json.load(new)
