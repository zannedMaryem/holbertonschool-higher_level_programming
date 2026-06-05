#!/usr/bin/python3
"""This module is to write int a file"""


def write_file(filename="", text=""):
    """This function writes a test into a file and returns
    the number of charachters written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        nb_of_char = f.write(text)
        return nb_of_char
