#!/usr/bin/python3
#computes square values of all integrs of a matrix
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
