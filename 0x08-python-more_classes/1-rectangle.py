#!/usr/bin/python3
""" define class rectangle"""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width: Width of the rectangle.
            height: height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer
            ValueError: TypeError: If width or height less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of rectangle

        Args:
            value (int): The new width.

        Raises:
            TaypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
