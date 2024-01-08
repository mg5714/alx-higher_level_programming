#!/usr/bin/python3
"""define module"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance.

    Args:
        obj: An object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
