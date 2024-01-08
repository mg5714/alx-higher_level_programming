#!/usr/bin/python3
"""define module"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance

    Args:
        obj: An object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """

    return type(obj) == a_class
