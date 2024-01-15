#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of Square.

        Args:
            size: The size of the square.
            x: x-coordinate of the square's position.
            y: y-coordinate of the square's position.
            id: Identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign attributes: id, size, x, y."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(min(len(args), len(attributes))):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
