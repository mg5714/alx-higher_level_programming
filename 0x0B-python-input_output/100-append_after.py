#!/usr/bin/python3
"""define module"""


def append_after(filename="", search_string="", new_string=""):
    """append new string, search string in file"""

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
