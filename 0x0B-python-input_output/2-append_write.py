#!/usr/bin/python3
""" a function to append text to file"""


def append_write(filename="", text=""):
    """ a function to append text to file"""
    with open(filename, mode="a") as f:
        f.write(text)
        return len(text)
