#!/usr/bin/python3
""" a function that writes json to file"""
import json


def load_from_json_file(filename):
    """ a function to load json from file"""
    with open(filename, mode='r') as f:
        return json.loads(f.read())
