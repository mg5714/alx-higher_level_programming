#!/usr/bin/python3


def lookup(obj):
    """
    Returns a list of available attributes.

    Args:
        obj: Any object.

    Returns:
        A list of strings containing the names of attributes.
    """
    return dir(obj)
