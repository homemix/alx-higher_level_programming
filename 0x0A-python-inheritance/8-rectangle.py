#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
a class for rectangles  
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ initialize the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
