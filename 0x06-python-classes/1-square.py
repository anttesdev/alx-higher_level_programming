#!/usr/bin/python3

""" Defining a class called Square"""


class Square:
    """ This is going to define a square """

    def __init__(self, size=0):
        """ This is initializing the instance of a square


        Args:
            size(int) the size of the new square created

            """
        self.__size = size
