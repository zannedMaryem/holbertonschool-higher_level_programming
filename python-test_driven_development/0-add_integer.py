#!/usr/bin/python3
"""
This module provides a function that adds two integers, 
ensuring type safety by raising a TypeError 
when inputs are not integers or floats.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: First number, must be int or float.
        b: Second number, must be int or float (default is 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
