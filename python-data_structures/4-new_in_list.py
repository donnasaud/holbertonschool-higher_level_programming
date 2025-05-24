#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Returns a new list with the element replaced at a given index.

    Does not modify the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
