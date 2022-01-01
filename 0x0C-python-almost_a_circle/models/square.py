#!/usr/bin/python3
"""
This module contains the square class
"""
from models import Rectangle


class Square(Rectangle):
    """ initialize the class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the class square with inherited properties"""
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    @property
    def size(self):
        """ getter getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ str representation of square class"""
        return "{} ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update the square with keyword and non keyword arguments."""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        """ return dictionary representation of square"""
        return self.__dict__
