#!/usr/bin/python3
#returns wighted average of all integers tuples
def weight_average(my_list=[]):
    if not my_list:
        return 0

    wei = 0
    den = 0

    for tup in my_list:
        wei += tup[0] * tup[1]
        den += tup[1]

    return (wei / den)
