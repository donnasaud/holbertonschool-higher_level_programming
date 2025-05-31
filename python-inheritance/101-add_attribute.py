#!/usr/bin/python3
"""Function to add attribute dynamically to an object."""


def add_attribute(obj, attr_name, value):
    """Adds a new attribute to an object if possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
