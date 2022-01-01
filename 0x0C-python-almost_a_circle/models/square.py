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
