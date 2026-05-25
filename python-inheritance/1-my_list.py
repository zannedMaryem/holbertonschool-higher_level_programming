#!/usr/bin/python3
""" Class that sorts a list"""


class MyList(list):
    """ Inherited class from list"""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)

        if isinstance(self, MyList):
            self[:] = sorted_list