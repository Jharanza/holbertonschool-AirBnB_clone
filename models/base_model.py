#!/usr/bin/python3
''' Module base for all '''
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__clase__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        text = "[{}] ({}) {}"
        return text.format(self.__class__.__name__, self.id, self.__dict__)
