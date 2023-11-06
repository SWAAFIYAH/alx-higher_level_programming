#!/usr/bin/python3
"""Defining class MyInt that inherits from int."""
class MyInt(int):
    """Inverting int operators == and !=."""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
