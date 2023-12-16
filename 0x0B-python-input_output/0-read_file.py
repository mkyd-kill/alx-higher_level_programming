#!/usr/bin/python3
"""
A function that reads a text file and
prints it to stdout
"""


def read_file(filename=""):
    """Takes a files, reads it and prints its content"""
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()
        print(contents, end="")
