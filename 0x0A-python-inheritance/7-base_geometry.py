#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """ a function to find area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
