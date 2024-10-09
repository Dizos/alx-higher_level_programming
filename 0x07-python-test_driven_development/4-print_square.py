#!/usr/bin/python3
"""
provides a function for printing a square using '#' characters.

The function takes a size parameter and prints a square of that size.
"""


def print_square(size):
    """
    Print a square of '#' characters.

    Args:
        size (int): The length of the square's sides.

    Raises:
        TypeError: If size is not an integer or if it's a float less than 0.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
