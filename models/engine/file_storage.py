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
        return FileStorage.__objects

    def new(self, obj):
        '''
            method that sets the object with a key
            Args:
                obj: object to set
        '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' method that seialize the object '''
        file_obj = FileStorage.__objects
        serial_obj = {key: obj.to_dict() for key, obj in file_obj.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        ''' method that deserialize the object '''
        data_dict = {}
        classes = {
            "BaseModel": BaseModel,
        }
        try:
            with open(self.__file_path, 'r') as file:
                data_dict = json.load(file)
                for key, value in data_dict.items():
                    self.__objects[key] = classes["__class__"]](**value)
        except FileNotFoundError:
            pass
