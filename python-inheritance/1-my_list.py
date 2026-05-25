#!/usr/bin/python3
""" Class that sorts a list"""


class MyList(list):
    """ Inherited class from list"""

    def print_sorted(self):
        """ a class methood to sort list"""
        print(sorted(self))