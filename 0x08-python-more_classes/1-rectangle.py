#!/usr/bin/python3

"""
A Rectangle class that defines a rectangle
"""


class Rectangle:
    """Rectangle class that defines a rectangle: width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width Getter method"""
        return self._width

    @width.setter
    def width(self, value):
        """width Setter value method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """height Getter method"""
        return self._height

    @height.setter
    def height(self, value):
        """height Setter value method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
