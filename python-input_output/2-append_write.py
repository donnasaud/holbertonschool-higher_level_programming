#!/usr/bin/python3

"""
This module contains a function that appends text to a UTF-8 file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends text to a UTF-8 file and returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

