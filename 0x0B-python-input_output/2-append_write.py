#!/usr/bin/python3
"""define function"""


def append_write(filename="", text=""):
    """ append string at end of the text"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
