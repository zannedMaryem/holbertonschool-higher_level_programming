#!/usr/bin/python3
""" Class that sorts a list"""


class MyList(list):
    """ Inherited class from list"""

    def __str__(self):
        """Return the string representation of the list."""
        return str(list(self))

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
