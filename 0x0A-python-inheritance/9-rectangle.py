#!/usr/bin/python3
"""
a class for rectangles  with inherited
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ initialize the class rectangle with height and width"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """ a function to calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return the description of the class rectangle"""
        return '[Rectangle] {:d}/{:d}'.format(self.__width, self.__height)
