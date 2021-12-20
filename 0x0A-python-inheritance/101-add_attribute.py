#!/usr/bin/python3
"""
    add a new attribute to class 
    Function that adds a new attribute to an object if it’s possible
"""


def add_attribute(cla, attribute, value):
    """Function that adds a new attribute to an object if it's possible"""
    if not (hasattr(cla, '__dict__')):
        raise TypeError("can't add new attribute")
    setattr(cla, attribute, value)
