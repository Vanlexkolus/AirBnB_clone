#!/usr/bin/python3
"""
module file_storage
This moulde conatian a class FileStorage
"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """
    class attr:
        __file_path
        __objects
    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __object"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __object:
            the obj with the key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serilaize __object to JSOn file"""
        my_dict = {}

        for key, obj in self.__objects.items():
            '''if type(obj) is dict:
            my_dict[key] = obj
            else'''
            my_dict[key] = obj.to_dict()
            with open(self.__file_path, 'w') as f:
                json.dump(my_dict, f)

    def reload(self):
        """deserialize the Json file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
                for key, value in new_obj.items():
                    class_name, obj_id = key.split('.')
                    cls = globals().get(class_name)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
