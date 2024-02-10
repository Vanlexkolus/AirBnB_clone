#!/usr/bin/env python3
import uuid
import datetime


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
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    if isinstance(value, str):
                        kwargs[key] = datetime.datetime.strptime(
                            value, '%Y-%m-%d %H:%M:%S')
                        print(f"{key} ---- {value}")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()

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
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance:
        """
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
