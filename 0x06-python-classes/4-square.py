#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An empty Square class
    """

    def __init__(self, size=0):
        """
        Initialize a Square class with attribute size.
        """
        self.__size = size

    @property
    def size(self):
        """ Get size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """ Return the area of the square"""
        return self.__size * self.__size
