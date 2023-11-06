!/usr/bin/python3
"""Defining object's attribute lookup function."""


def lookup(obj):
    """Return list for object's available attributes."""
    return (dir(obj))
