#!/usr/bin/python3
""" define add_attribute method"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
