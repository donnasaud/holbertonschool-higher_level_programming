#!/usr/bin/python3
"""
This module defines a class BaseGeometry with validation methods.
"""


class BaseGeometry:
    """
    BaseGeometry defines a base class for geometry operations.
    """

    def area(self):
        """
        Raises an Exception to indicate area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): the name of the variable (for error messages)
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
