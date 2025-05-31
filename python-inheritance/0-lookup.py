#!/usr/bin/python3
"""
This module provides a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: Any Python object (class, instance, etc.)

    Returns:
        list: A list of names (strings) of the available attributes
        and methods.
    """
    return dir(obj)
