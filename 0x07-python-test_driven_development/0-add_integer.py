#!/usr/bin/python3
"""
provides a function for integer addition.

The module has a function that adds two numbers,
making them to integers if they are floats.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
