#!/usr/bin/python3

def write_file(filename="", text=""):
    """ a function to write_file and return the length of the file"""
    with open(filename, mode="w") as f:
        f.write(text)
        return len(text)
