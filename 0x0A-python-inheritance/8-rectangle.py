#!/usr/bin/python3
"""
Import a super class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
