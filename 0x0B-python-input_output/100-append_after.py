#!/usr/bin/python3
"""Defining text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing given string in a file.

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as m:
        for line in m:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
