#!/usr/bin/python3

def read_file(filename=""):
    """ A function to raed a file and print it to  output"""
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(),end='')
