#!/usr/bin/python3

"""
a class MyList that inherits from list
"""


class MyList(list):
    """a function that prints the list, in ascending sort"""
    def print_sorted(self):
        print(sorted(self))
