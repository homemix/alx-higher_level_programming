#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class.
"""


class Rectangle:
    """A simple Rectangle class"""
    number_of_instances = 0
    print_symbol ='#'

    def __init__(self, width=0, height=0):
        """ a rectangle initializes a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width of the rectangle getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width of rectangle setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of rectangle getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height of rectangle setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculate the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            perimeter_rectangle = 0
        else:
            perimeter_rectangle = 2 * (self.__width + self.__height)
        return perimeter_rectangle

    def __str__(self):
        """ string representation of rectangle class"""
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        for h in range(self.__height):
            for w in range(self.__width):
                new_str += str(self.print_symbol)
            if h != self.__height - 1:
                new_str += '\n'
        return new_str

    def __repr__(self):
        """ a self replicating method"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """ a self destructuring method"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
