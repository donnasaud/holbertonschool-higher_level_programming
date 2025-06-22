#!/usr/bin/python3
"""
This module contains a function that writes a string
to a UTF-8 text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes text to a UTF-8 file and returns number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
