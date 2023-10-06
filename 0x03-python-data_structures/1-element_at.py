#!/usr/bin/python3
#retrieves element from list

def element_at(my_list, idx):
    """retrive element from list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
