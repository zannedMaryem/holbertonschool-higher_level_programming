#!/usr/bin/python3
""" This module is to check whether on object is 
an instance of a class"""


def is_same_class(obj, a_class):
    """" A function that tests if the object is
     exactly an instance of the specified class"""
    return isinstance(obj, a_class)
