#!/usr/bin/python3
"""define module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
