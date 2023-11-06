#!/usr/bin/python3
"""Defining inherited list class MyList."""


class MyList(list):
    """Implementing sorted printing for built-in list class."""

    def print_sorted(self):
        """Print list in a sorted ascending order."""
        print(sorted(self))
