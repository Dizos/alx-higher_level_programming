#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """is a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If the  size is not an integer.
            ValueError: If  the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
