#!/usr/bin/python3
""" Defining a class called Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the instance of a square"""
        self.size = size

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        if type(value) not in [int, float]:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def __eq__(self, another):
        """Equal comparator"""
        return self.area() == another.area()

    def __ne__(self, another):
        """Not equal comparator"""
        return self.area() != another.area()

    def __lt__(self, another):
        """Less than comparator"""
        return self.area() < another.area()

    def __le__(self, another):
        """Less than or equal comparator"""
        return self.area() <= another.area()

    def __gt__(self, another):
        """Greater than comparator"""
        return self.area() > another.area()

    def __ge__(self, another):
        """Greater than or equal comparator"""
        return self.area() >= another.area()
