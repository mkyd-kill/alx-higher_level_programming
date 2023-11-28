#!/usr/bin/python3

"""
Class that prevents the user from dynamically creating
new instance attributes
"""


class LockedClass:
    """prevents from creating user"""
    __slots__ = ["firstname"]
