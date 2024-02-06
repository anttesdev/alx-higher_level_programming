#!/usr/bin/python3
"""
A module that appends text to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends text to a file
    Args:
        filename: name of the file
        text(str): text to be appended
    """
    with open(filename, 'a', encoding='utf-8') as new:
        return new.write(text)
