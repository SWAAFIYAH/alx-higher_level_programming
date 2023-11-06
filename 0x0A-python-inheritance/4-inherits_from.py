#!/usr/bin/python3
"""Defining inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of class.

    Args:
        obj (any): object to check.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        If not - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
