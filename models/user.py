#!/usr/bin/python3
from models.base_model import BaseModel
"""Module to instance a user"""


class User(BaseModel):
    """class User with public attributes inherits from BaseModel
    Attributes:
    email: email of User
    password: password of User
    First_name: first name of User
    last_name: last name of User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
