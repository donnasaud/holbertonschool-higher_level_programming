#!/usr/bin/python3
"""Defines a class Square that supports rich comparisons."""


class Square:
    """Represents a square with size and area comparisons."""

    def __init__(self, size=0):
        """Initialize the square with validated size."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size; must be a number >= 0."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less-than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less-than or equal based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater-than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater-than or equal based on area."""
        return self.area() >= other.area()
