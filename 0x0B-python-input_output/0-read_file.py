#!/usr/bin/python3
"""Module for reading and printing file contents."""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
