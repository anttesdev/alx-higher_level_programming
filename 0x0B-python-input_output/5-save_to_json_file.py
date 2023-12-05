#!/usr/bin/python3
"""
A module that writes an object to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    Args:
        my_obj: the object
        filename: the file to write the object to
    """
    with open(filename, 'w', encoding='utf-8') as new:
        json.dump(my_obj, new)
