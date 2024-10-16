#!/usr/bin/python3
"""Module that contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object."""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        A dictionary description of the object
    """
    return obj.__dict__
