#!/usr/bin/python3
""" define class rectangle"""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self._width = width
        self._height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates and returns the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the rectangle's perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a visual representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return (Rectangle.print_symbol * self.width + "\n") * self.height

    def __repr__(self):
        """Returns a string representation for recreating the instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when the rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
