#!/usr/bin/python3
"""
Inserts a line of text to a file
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a new line string to a file"""
    with open(filename, "r") as file:
        file_lines = []
        for line in file:
            file_lines.append(line)
            if line.find(search_strings) != -1:
                file_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(file_lines)
