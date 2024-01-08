#!/usr/bin/python3
"""define module"""


class BaseGeometry:
    """Empty class for geometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
