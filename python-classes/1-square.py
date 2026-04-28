#!/usr/bin/python3
"""
This module defines a Square class.
The Square class is used to represent a geometric square
with a specific size attribute.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The side length of the square.
        """
        self.__size = size
