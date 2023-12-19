#!/usr/bin/python3
"""Square class"""


class Square:
    """ def a square """

    def __init__(self, size=0):
        """
        initialize a square obj with a given size.

        Args:
            size: side length of square
        """
        self.__size = size

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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area (integer).
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
