#!/usr/bin/python3
"""
A function that reads a text from a file
"""


def read_file(filename=""):
    """
    A function that reads text from a file
    Args:
        filename(str): the name of the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data, end="")
