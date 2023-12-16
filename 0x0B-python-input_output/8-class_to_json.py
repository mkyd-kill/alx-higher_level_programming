#!/usr/bin/python3
"""
Returns the dictionary description for a json
serialized object
"""


def class_to_json(obj):
    """returns the description of the object"""
    return obj.__dict__
