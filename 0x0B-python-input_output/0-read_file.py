#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """ A function to raed a file and print it to  output"""
    with open(filename, encoding="utf-8", mode="r") as f:
        print(f.read(), end='')
