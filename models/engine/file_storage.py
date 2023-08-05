#!/usr/bin/python3
'''
    module file_storage that serialize and deserialize files
'''
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' return the object like a dictionary '''
        return self.__objects

    def new(self, obj):
        '''
            method that sets the object with a key
            Args:
                obj: object to set
        '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' method that seialize the object '''
        data = {}
        for k, v in self_obj.items()
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, file)

    def reload(self):
        ''' method that deserialize the object '''
        data_dict = {}
        classes = {
            "BaseModel": BaseModel,
        }
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    self.__objects[k] = classes["__class__"]](**v)
        except FileNotFoundError:
            pass
