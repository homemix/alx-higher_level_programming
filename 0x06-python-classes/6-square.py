#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """An empty Square class
    """

    def __init__(self, size=0, position=(0, 0)):
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

    def my_print(self):
        """ Print square in #"""
        if self.__size == 0:
            print()
        else:
            for r in range(self.__size):
                for c in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """ setter for position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """getter for position property"""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
