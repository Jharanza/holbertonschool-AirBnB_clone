#!/usr/bin/python3
''' module to instance a user '''
from modeels.base_model import BaseModel


class User(BaseModel):
    ''' class User with public attributes '''
    self.mail = ''
    self.password = ''
    self.first_name = ''
    self.last_name = ''


