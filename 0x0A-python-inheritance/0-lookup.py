#!/usr/bin/python3
"""
This module creates a way to lookup attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to view.

    Returns:
        A list of strings representing the attributes and methods of the object.
    """
    return dir(obj)
