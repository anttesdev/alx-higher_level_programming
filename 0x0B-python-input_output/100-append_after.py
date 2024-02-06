#!/usr/bin/python3
"""
A function that inserts a text in to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line
    containing a specific string in a file.
    arguments:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each
        line containing the search string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
