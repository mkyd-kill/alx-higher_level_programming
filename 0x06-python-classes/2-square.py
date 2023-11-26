#!/usr/bin/python3

"""
Class Instantiation Square with attribute type checker
"""


class Square:
    """class iniialization with init"""
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._size = size
