#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module is for defining basic geometry"""


class Rectangle(BaseGeometry):
    """this class defines a rectangle"""

    def __init__(self, width, height):
        """Init method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
