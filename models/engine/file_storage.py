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
        key = "{}.{}".format(__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serilaize __object to JSOn file"""
        json_string = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json_string)

    def reload(self):
        """deserialize the Json file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.loads(f.read())
