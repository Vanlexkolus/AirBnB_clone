#!/usr/bin/python3
from base_model import BaseModel


class User(BaseModel):
    """
    This is a class named user that inherits from
    the class BaseMode, it will be used to create
    Public class attributes below for Task 8
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
