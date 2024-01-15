#!/usr/bin/python3
"""Module for square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square shape"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance"""
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """Returns a string of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size of square"""
        self.width = value
        self.height = value
