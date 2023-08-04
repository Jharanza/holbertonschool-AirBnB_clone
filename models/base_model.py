#!/usr/bin/python3
''' Module base for the files of the proyect '''
from datetime import datetime


class BaseModel:
    ''' class that assign an id to an object, update
    the date the time is called and manipulate the method
    dict. Count with 4 methods:
        constructor
        save
        to_dict
        to_str
    '''
    def __init__(self):
        ''' method constructor that assign an unique id to an object '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        ''' method public that update the attribute updates_at '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' method public that manipulate the method dict() '''
        my_dict = self.__dict__.copy()
        my_dict['__clase__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        ''' method overwrite to represent the object '''
        text = "[{}] ({}) {}"
        return text.format(self.__class__.__name__, self.id, self.__dict__)
