#!/usr/bin/python3
"""
This module defines a function that prints text with indentation rules.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: '.', '?' and ':'.

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Split into lines, strip spaces at start/end of each line
    lines = [line.strip() for line in result.split("\n")]
    for line in lines:
        if line:  # avoid printing empty lines caused by split
            print(line, end="")
