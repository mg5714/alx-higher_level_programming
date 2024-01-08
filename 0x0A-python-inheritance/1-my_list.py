#!/usr/bin/python3
"""module define"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """ fun to print sorted"""
        print(sorted(self))
