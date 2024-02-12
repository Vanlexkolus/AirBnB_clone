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
        key = "{}.{}".format(obj.__class__.name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serilaize __object to JSOn file"""
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    def reload(self):
        """deserialize the Json file to __objects"""
        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for key, val in tmp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileFOundError:
            pass 
