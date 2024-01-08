#!/usr/bin/python3
"""define module"""


class BaseGeometry:
    """Empty class for geometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Class Rectangle inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Return a string representation of the rectangle using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"


class Square(Rectangle):
    """Class Square inherits from Rectangle."""

    def __init__(self, size):
        """Initialize the Square instance with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"

    def __repr__(self):
        """Return a string representation of square using eval()."""
        return f"Square({self._Rectangle__width})"
