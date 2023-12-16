#!/usr/bin/python3
"""
Adds arguments to python list,
and saves them to a file
"""
from os import path
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
try:
    contents = load_from_json_file(file)
except FileNotFoundError:
    contents = []
for i in range(1, len(argv)):
    contents.append(argv[i])
save_to_json_file(contents, file)
