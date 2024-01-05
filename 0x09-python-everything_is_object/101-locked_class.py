#!/usr/bin/python3
"""module in it locked class"""
class LockedClass:
    """Allow only "first_name" attribute"""
    __slots__ = ["first_name"]
