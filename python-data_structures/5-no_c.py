#!/usr/bin/python3
def no_c(my_string):
    """Returns a new string with all 'c' and 'C' characters removed."""
    return "".join(char for char in my_string if char != 'c' and char != 'C')
