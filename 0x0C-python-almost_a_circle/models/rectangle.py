#!/usr/bin/python3
"""
This module contains the Rectangle class
"""
from models import Base


class Rectangle(Base):
    """ initialize the representation class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the representation class rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ The getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ te setter of width"""
        self.__width = value

    @property
    def height(self):
        """ the getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ the setter of height"""
        self.__height = value

    @property
    def x(self):
        """ the getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """the setter of x"""
        self.__x = value

    @property
    def y(self):
        """" the getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ the setter of y"""
        self.__y = value
