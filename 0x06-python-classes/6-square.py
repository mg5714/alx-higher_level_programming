#!/usr/bin/python3
"""Square class"""


class Square:
    """ def a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize a square obj with a given size.

        Args:
            size: side length of square
            position: position of the square as a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        property for side of square.

        Raises:
            TypeError: if size not int.
            ValueError: if size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ return position of square """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter position

        Args:
            value: The new position of the square.

        Raises:
            TypeError:  position must be a tuple of 2 positive.
        """
        if not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area (integer).
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
