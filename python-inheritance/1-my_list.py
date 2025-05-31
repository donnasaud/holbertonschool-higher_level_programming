#!/usr/bin/python3
"""
This module defines a subclass of list called MyList.
MyList has a public method that prints the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList is a subclass of list with an added print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
