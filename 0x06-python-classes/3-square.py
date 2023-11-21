#!/usr/bin/python3

""" Defining a class called Square"""


class Square:
    """ This is going to define a square """

    def __init__(self, size=0):
        """ This is initializing the instance of a square


        Args:
            size(int) the size of the new square created

            """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """ This is a public instance method calculating the area of a square

        Args:
            self: is the object itself

            """
        return self.__size * self.__size
