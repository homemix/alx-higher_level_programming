#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An empty Square class
    """

    def __init__(self, size=0):
        """
        Initialize a Square class with attribute size.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        
