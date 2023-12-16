#!/usr/bin/python3
"""
Student class
"""


class Student:
    """a class defining a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves the obj representation"""
        if attrs is None:
            return self.__dict__
        contents = {}
        for i in attrs:
            if i in self.__dict__ and type(i) is str:
                contents[i] = self.__dict__.get(i)
        return contents
