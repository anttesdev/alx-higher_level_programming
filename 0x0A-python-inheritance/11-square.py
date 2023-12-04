#!/usr/bin/python3
"""
Define a Square class that inherits from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A formatted string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
