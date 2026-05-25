#!/usr/bin/python3
"""This is an empty Module"""


class BaseGeometry():
    """This is an empty class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates a value"""
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        self.value = value