#!/usr/bin/python3
"""This module is for defining an animal """


from abc import ABC, abstractmethod


class Animal(ABC):
    """This class defines an animal by it's sound"""

    @abstractmethod
    def sound(self):
        """This method defines animal sound"""
        pass

class Dog(Animal):
    """This class defines a dog"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"

class Cat(Animal):
    """This class defines a cat"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
