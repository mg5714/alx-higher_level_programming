#!/usr/bin/python3
""" define MyInt class"""


class MyInt(int):
    """Class MyInt inherits from int with inverted == and != operators"""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
