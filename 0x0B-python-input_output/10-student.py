#!/usr/bin/python3
""" A student class defines student """


class Student:
    """ A student class defines student class """

    def __init__(self, first_name, last_name, age):
        """ initialize the student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return the dictionary representation"""
        d = vars(self)
        if attrs is None:
            return d
        new_d = {}
        for k in d:
            if k in attrs:
                new_d[k] = d[k]
        return new_d
