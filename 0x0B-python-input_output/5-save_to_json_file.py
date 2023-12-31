#!/usr/bin/python3
"""
Writes and object to a text file
using json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes a json object to a file"""
    with open(filename, "w") as filename:
        json.dump(my_obj, filename)
