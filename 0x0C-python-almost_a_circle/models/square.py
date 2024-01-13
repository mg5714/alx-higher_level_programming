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

    def updateed(self, id=None, size=None, x=None, y=None):
        """update attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates attributes of the square"""
        if args:
            self.updateed(*args)
        elif kwargs:
            self.updateed(**kwargs)

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
