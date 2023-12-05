#!/usr/bin/python3

"""
A function that writes text in to a file
and returns the number of Chars in the text
"""


def write_file(filename="", text=""):
    """
    Function that writes text to a file
    Args:
        filename: the name of the file
        text(str): the text to be written to the file
    Returns: the number of Chars in the file
    """
    with open(filename, 'w', encoding='utf-8') as new:
        return new.write(text)
