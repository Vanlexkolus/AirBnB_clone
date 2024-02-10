#!/usr/bin/python3
"""
Module base_model
This module contain base class(BaseNodel).
The BaseModel class contain attr and method common to all classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    The BaseModel is a class that defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of public attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime
                                (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        This method prints:
        [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"{[self.__class__.__name__]}, {(self.id)}, {self.__dict__}")

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
