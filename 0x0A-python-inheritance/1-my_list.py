#!/usr/bin/python3

""" Defines a class MyList that inherits from list"""


class MyList(list):
    """
    A class that inherits a list and implements sorting
    """

    def print_sorted(self):
        sort = sorted(self)
        print(sort)
