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
        """ save json dictionary to file"""
        with open(cls.__name__ + '.json', 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string())

    def from_json_string(json_string):
        """convert to json file and return"""
        if len(json_string) == 0 or json_string is None:
            return '[]'
        return json.dumps(json_string)

    def create(cls, **dictionary):
        """returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    def load_from_file(cls):
        """ load file from json and print it"""
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()
            a_list = cls.from_json_string(content_string)
            list_instances = []
            for i in range(len(a_list)):
                list_instances.append(cls.create(**a_list[i]))
        except:
            list_instances = []

        return list_instances
