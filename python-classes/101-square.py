#!/usr/bin/python3
"""Defines a class Square that supports printing via __str__."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, validating it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, validating it's a tuple of 2 positive integers."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character, respecting position."""
        if self.__size == 0:
            print()
            return

        print(str(self), end="")

    def __str__(self):
        """Return the string representation of the square."""
        if self.__size == 0:
            return "\n"

        result = []
        result.extend(["\n"] * self.__position[1])

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            result.append(line)

        return "\n".join(result) + "\n"
