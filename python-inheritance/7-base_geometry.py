#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods."""

    def area(self):
        """Raises an exception that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer greater than 0.

        Args:
            name (str): Name of the value.
            value (int): Value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
