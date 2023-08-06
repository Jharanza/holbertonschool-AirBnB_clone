#!/usr/bin/python3
''' method that instance a city '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' class with two public attributes '''
    state_id = ''
    name = ''
