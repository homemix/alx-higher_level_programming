#!/usr/bin/python3
"""
This module contains the "Base" class
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ convert list of dictionaries to json string"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with open(cls.__name__+'.json', 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string())
        