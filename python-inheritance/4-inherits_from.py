#!/usr/bin/python3
"""
This module defines a function that checks if an object is
an instance of a subclass (not the class itself) of a given class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class.
    Returns False if obj is an instance of a_class itself or not related.

    Args:
        obj: The object to check.
        a_class: The reference class.

    Returns:
        bool: True if obj inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
