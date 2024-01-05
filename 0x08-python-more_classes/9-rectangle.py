#!/usr/bin/python3
""" define class rectangle"""


class Rectangle:
    """Represents a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle

        Args:
            width: Width of the rectangle.
            height: height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer
            ValueError: TypeError: If width or height less than 0
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """ sets height

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

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            symbol_line = str(self.print_symbol) * self.__width
            return "\n".join(symbol_line for i in range(self.__height))

    def __repr__(self):
        """Return a representation of the rectangle for recreation using eval()
        """
        return "{:s}({:d}, {:d})".format((type(self).__name__),
                self.__width, self.__height)
    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger or equal area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Create a new Rectangle instance.

        Args:
            size: The width and height of the new Rectangle.
        """
        return cls(size, size)
