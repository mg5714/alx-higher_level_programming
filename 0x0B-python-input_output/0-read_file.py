#!/usr/bin/python3
"""define module"""


def read_file(filename=""):
    """ read text file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
