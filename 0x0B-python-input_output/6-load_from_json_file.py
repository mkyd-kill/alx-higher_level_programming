#!/usr/bin/python3
"""
Creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """creates object from a json file"""
    with open(filename, "r") as file:
        return json.load(file)
