#!/usr/bin/python3
"""
Module base_model
This module contain base class(BaseNodel).
The BaseModel class contain attr and method common to all classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base clas for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of public attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        This method prints:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"{[self.__class__.__name__]}, ({self.id}), {self.__dict__}")

    def __repr__(self):
        """
        return string representation
        """
        return (self.__str__())

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
