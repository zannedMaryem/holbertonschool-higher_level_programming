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

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            # print the current buffer (stripped of leading/trailing spaces)
            print(buffer.strip(), end="\n\n")
            buffer = ""  # reset buffer

    # print any leftover text (if it doesn't end with . ? :)
    if buffer.strip():
        print(buffer.strip(), end="")
