#!/usr/bin/python3
"""
This module provides a function that reads and prints
the contents of a UTF-8 text file.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
