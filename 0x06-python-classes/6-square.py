#!/usr/bin/python3
"""This module defines an advanced Square class."""

class Square:
    """A class that defines a square by its size and position.
    Attributes:
        __size (int): The size of the square's sides.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.
        Returns:
            int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters.
        If size is 0, prints an empty line.
        Uses position for indentation and vertical offset.
        """
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)