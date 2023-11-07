#!/usr/bin/python3
"""Defining Python class-to-JSON function."""
def class_to_json(obj):
    """Returns dictionary represntation of simple data structure."""
    return obj.__dict__
