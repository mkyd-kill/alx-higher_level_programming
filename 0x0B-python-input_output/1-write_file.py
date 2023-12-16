#!/usr/bin/python3
"""
A function that reads a text file and
returns number of characters used
"""


def write_file(filename="", text=""):
    """Takes a files, reads it and returns character number"""
    with open(filename, "w", encoding="utf-8") as file:
        contents = file.write(text)
    return contents
