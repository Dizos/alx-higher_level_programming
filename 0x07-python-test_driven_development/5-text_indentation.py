#!/usr/bin/python3
"""
provides a function for formatting text with specific indentation rules.

The function adds two newlines after each of these characters: '.', '?' and ':'.
It also removes leading and trailing spaces from each line.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?' and ':'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    current_line = ""
    
    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()
            current_line = ""
    
    if current_line:
        print(current_line.strip(), end="")
