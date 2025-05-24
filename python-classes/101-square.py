#!/usr/bin/python3
"""Defines a class Square that prints itself with '#' and position."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size, must be an integer >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position, must be a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or not isinstance(value[1], int) or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character and position offsets."""
        if self.__size == 0:
            print()
            return
        print(self.__str__())

    def __str__(self):
        """Return the square as a string with '#' and position offsets."""
        if self.__size == 0:
            return ""

        lines = []
        # Vertical offset
        lines.extend(["" for _ in range(self.__position[1])])

        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)

        return "\n".join(lines)
