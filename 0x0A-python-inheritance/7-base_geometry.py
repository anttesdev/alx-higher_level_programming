#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    This is a base class for geometry-related classes.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it is an integer greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
