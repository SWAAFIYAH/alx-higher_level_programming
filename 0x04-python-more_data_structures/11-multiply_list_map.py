#!/usr/bin/python3
#multiplies the values of a list
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))

