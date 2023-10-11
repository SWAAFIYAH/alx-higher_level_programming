#!/usr/bin/python3
#prints a dictionary in orderd keys
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for x in list_ord:
        print("{}: {}".format(x, a_dictionary.get(x)))
