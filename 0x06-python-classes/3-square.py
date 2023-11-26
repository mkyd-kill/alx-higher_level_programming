#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """Class initialization with init"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """Public instance method area that returns the current square area"""
        def area(self):
            return self._size * self._size
