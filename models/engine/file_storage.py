#!/usr/bin/python3
"""
module file_storage
This moulde conatian a class FileStorage
"""
import json
import os


class FileStorage:
    """
    class attr:
        __file_path
        __objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __object"""
        return cls.__objects

    def new(self, obj):
        """set in __object:
            the obj with the key <obj class name>.id
        """
        key = __class__.__name__.id
        cls.__objects[key] = obj

    def save(self):
        """serilaize __object to JSOn file"""
        json_string = json.dumps(cls.__objects)
        with open('cls.__file_path', 'w') as f:
            f.write(json_string)

    def reload(self):
        """deserialize the Json file to __objects"""
        if os.path.exists(cls.__file_path):
            with open('cls.__file_path', 'r') as f:
                json_dict = json.loads(f.read())
