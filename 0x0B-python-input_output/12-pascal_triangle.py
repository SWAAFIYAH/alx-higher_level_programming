#!/usr/bin/python3
"""Defining Pascal's Triangle function."""


def pascal_triangle(n):
    """Representing Pascal's Triangle of size n.

    Returning list of lists of integers representing triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
