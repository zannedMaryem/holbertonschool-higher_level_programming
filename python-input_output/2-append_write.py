#!/usr/bin/python3
"""This module is for appending test in a file"""


def append_write(filename="", text=""):
    """This function append a text in a file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        nb = file.write(text)
        return nb
