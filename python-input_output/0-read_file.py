#!/usr/bin/python3
"""This module is intended to open a file"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
