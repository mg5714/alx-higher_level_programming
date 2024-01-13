#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes new instance of Rectangle class.

        Args:
            width: width of rectangle.
            height: height of rectangle.
            x: x-coordinate of rectangle's position.
            y: y-coordinate of rectangle's position.
            id: identifier for rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute.

        Args:
            value: The new width value.
        """
        self.validate_or_non("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute.

        Args:
            value: The new height value.
        """
        self.validate_or_non("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute.

        Args:
            value: The new x value.
        """
        self.validate_or_non("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute.

        Args:
            value: The new y value.
        """
        self.validate_or_non("y", value)
        self.__y = value

    def validate_or_non(self, name, value, eq=True):
        """Validates if the value is an integer or psative or vegative"""
        is type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not eq and value <= 0 :
            raise ValueError(f"{name} must be > 0")

    def area(self):
        """calculat area"""
        return self.width * self.height

    def display(self):
        """print str"""
        rect_str = '\n' * self.y + \
                (' ' * self.x + '#' * self.width + '\n') * self.height
        print(rect_str, end='')

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def updateed(self, id=None, width=None, height=None, x=None, y=None):
        """update attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates attributes of the rectangle."""
        if args:
            self.updateed(*args)
        elif kwargs:
            self.updateed(**kwargs)

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
