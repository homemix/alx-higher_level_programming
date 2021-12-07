#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An empty Square class
    """

    def __init__(self, size=0):
        """
        Initialize a Square class with attribute size.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        self.__size = size
