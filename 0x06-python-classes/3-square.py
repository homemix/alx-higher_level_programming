#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An empty Square class
    """

    def __init__(self, size=0):
        """
        Initialize a Square class with attribute size.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Return the area of the square"""
        return self.__size ** 2


