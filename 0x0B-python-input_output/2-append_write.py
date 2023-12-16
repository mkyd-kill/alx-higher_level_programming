#!/usr/bin/python3
"""
A function that appends a string at the end
of a text file and returns the number of
characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end and returns character number"""
    with open(filename, "a", encoding="utf-8") as file:
        contents = file.write(text)
    return contents
