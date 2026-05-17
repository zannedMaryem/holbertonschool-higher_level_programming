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

    for i, char in enumerate(text):
        buffer += char

        if char in ".?:":
            print(buffer.strip(), end="")

            # only print 2 new lines if there's more text after
            if i != len(text) - 1:
                print("\n")

            buffer = ""

    if buffer.strip():
        print(buffer.strip(), end="")
