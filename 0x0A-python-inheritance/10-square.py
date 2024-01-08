#!/usr/bin/python3
"""define module"""

Rectangle = __import__('9-rectangle').Rectangle


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
