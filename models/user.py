#!/usr/bin/python3
''' module to instance a user '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' class User with public attributes inherits from BaseModel'''
    def __init__(self, *args, **kvargs):
        ''' Using emthod super to call '''
        super().__init__(*args, **Kwargs)    
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
