#!/usr/bin/python3
""" a function that deserializes object"""
import json


def from_json_string(my_str):
    """ A function that deserializes object"""
    return json.loads(my_str)
