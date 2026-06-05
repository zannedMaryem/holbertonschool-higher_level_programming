#!/usr/bin/python3
"""This module is to create a student class"""


class Student():
    """This class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        self.__dict__.update(json)
