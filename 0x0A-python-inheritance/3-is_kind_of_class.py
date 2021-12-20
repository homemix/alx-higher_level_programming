#!/usr/bin/python3
"""
a function to check if the object is instance of class
"""


def is_kind_of_class(obj, a_class):
    """ check the instance of an object"""
    if isinstance(obj, a_class):
        return True
    return False
