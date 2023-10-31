#!/usr/bin/python3
#define a function for integer addition
def add_integer(a, b=98):
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an ineger")
    return (int(a) + int(b))
