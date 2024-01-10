#!/usr/bin/python3
"""Module for print_square"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size: is size length of the sqiare

    raises:
        TypeError: if size not an integer
        ValueError: if size less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
