#!/usr/bin/python3
""" define magicclass """

import math

class MagicClass:
    """ represent circale """

    def __init__(self, radius=0):
        """ init a magic class

        Args:
            radius: radius of new magicclass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("")
        self.__radius = radius

    def area(self):
        """ 
        return the area of magic circle
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        return circumference of magic circle
        """
        return (2 * math.pi * self.__radius)
