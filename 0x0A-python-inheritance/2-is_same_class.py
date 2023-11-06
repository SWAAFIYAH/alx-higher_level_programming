#!/usr/bin/python3
"""Defining class-checking function."""


def is_same_class(obj, a_class):
    """Check if object is exactly instance of given class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is exactly instance of a_class - True.
        If not - False.
    """
    if type(obj) == a_class:
        return True
    return False
