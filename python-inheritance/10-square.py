#!/usr/bin/python3
"""This module is for defining basic a square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square"""

    def __init__(self, size):
        """Init method for square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method to calculate square area"""
        return self.__size ** 2
    