#!/usr/bin/python3
''' module to instance a user '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' class User with public attributes '''
    mail = ''
    password = ''
    first_name = ''
    last_name = ''
