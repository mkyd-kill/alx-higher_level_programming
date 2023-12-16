#!/usr/bin/python3
"""
Returns an object representation of a json
"""
import json


def from_json_string(my_obj):
    """Returns an object from a json"""
    return json.loads(my_obj)
