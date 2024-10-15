#!/usr/bin/python3
"""Module for writing to a text file."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)