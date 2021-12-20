# !/usr/bin/python3
"""
A class to print sored list
"""


class MyList(list):
    """ a class to print a list"""

    def __init__(self):
        """ initialize the class"""
        super().__init__()

    def print_sorted(self):
        """ print the sorted list"""
        print(sorted(self))
