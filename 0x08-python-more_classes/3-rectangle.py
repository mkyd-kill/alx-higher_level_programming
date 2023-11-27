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
        return self.__width

    @width.setter
    def width(self, value):
        """width Setter value method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height Getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height Setter value method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints out the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for i in range(self.__height))
