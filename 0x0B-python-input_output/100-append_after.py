#!/usr/bin/python3
"""define module"""


def append_after(filename="", search_string="", new_string=""):
    """append new string, search string in file"""

    with open(filename, 'r', encoding='utf-8') as file:
        lines = []
        for line in file:
            if line == "":
                break
            line.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)
