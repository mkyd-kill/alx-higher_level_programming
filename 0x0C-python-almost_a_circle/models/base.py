#!/usr/bin/python3
"""
The Base class
"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        self.__nb_objects =+ 1
        self.id = self.__nb_objects
