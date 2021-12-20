# !/usr/bin/python3
"""
A class to print sored list 
"""


class MyList(list):
    """ a class to print a list"""

    def print_sorted(self):
        """ print the sorted list"""
        print(sorted(self))
