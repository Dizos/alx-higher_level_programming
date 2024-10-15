#!/usr/bin/python3
"""Module for converting a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        object: A Python object (e.g., dict, list) represented by the JSON string.
    """
    return json.loads(my_str)
