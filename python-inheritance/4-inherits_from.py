#!/usr/bin/python3
"""Function that checks inheritance relationship."""

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class; otherwise False.

    - Returns False when obj is an instance of a_class itself.
    - Returns False when a_class is not a class.
    """
    if not isinstance(a_class, type):
        return False
    obj_type = type(obj)
    return obj_type is not a_class and issubclass(obj_type, a_class)
