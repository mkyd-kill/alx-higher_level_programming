#!/usr/bin/python3
"""
Writes and object to a text file
using json representation
"""
import json


def save_to_json_file(obj, filename):
    """writes a json object to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dumps(obj, file)
