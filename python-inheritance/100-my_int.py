#!/usr/bin/python3
"""MyInt is a rebel that inverts == and !="""


class MyInt(int):
    """A subclass of int with inverted equality operators"""

    def __eq__(self, other):
        """Invert the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator"""
        return super().__eq__(other)

