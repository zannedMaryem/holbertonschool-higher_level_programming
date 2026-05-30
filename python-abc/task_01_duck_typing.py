#!/usr/bin/python3
"""This module is for defining a shape """


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """This class is for defining shapes"""

    @abstractmethod
    def area(self):
        """defines the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """defines the perimeter of the shape"""
        pass


class Circle(Shape):
    """A class that defines a circle"""

    def __init__(self, radius):
        """The constructor method for a circle"""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.radius = radius

    def area(self):
        """ Returns the area of a circle"""
        return self.radius ** 2 * pi

    def perimeter(self):
        """Returns the perimeter of a circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """A class that defines a rectangle"""

    def __init__(self, width, height):
        """The constructor method for a rectangle"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be > 0")
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimiter of a rectangle"""
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """A function that prints the area and
    perimeter of a given shape"""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")

circle = Circle(5)
rectangle = Rectangle(5, 8)

shape_info(circle)
shape_info(rectangle)
