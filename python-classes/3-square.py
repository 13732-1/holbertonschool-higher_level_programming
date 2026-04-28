#!/usr/bin/python3
"""
This module defines a Square class.
It includes validation for the size attribute and a method
to calculate the area of the square.
"""


class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the current square's area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
