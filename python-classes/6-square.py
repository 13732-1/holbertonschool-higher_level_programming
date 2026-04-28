#!/usr/bin/python3
"""
This module defines a Square class.
It includes validation for size and position, area calculation,
and a method to print the square at a specific coordinate position.
"""


class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The side length of the square.
        __position (tuple): The (x, y) coordinates for printing the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): The (x, y) coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The (x, y) coordinates of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): A tuple containing 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square's area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout using the '#' character and position.
        If size is 0, it prints an empty line.
        Position[1] adds new lines; Position[0] adds spaces.
        """
        if self.__size == 0:
            print("")
            return

        # Print the vertical offset (y-coordinate)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Print the square with horizontal offset (x-coordinate)
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
