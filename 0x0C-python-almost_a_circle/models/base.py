#!/usr/bin/python3
"""
Define a base class
"""


import json


class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Parameters:
        - id (int, optional): If provided, assign it to the id attribute.
          If not provided, increment the object
          counter and assign the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
