#!/usr/bin/python3
"""This module defines a function to convert a class
object to a JSON-serializable dictionary"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        The __dict__ attribute of the object containing all its attributes
    """
    return obj.__dict__
