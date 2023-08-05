#!/usr/bin/python3
'''
    module file_storage that serialize and deserialize files
'''
import json


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' return the object like a dictionary '''
        return fileStorage.__objects

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
        with open(FileStorage.__file.path, 'w') as file:
            json.dump(serial_obj, file)

    def reload(self):
        ''' method that deserialize the object '''
        try:
            with open(FileStorage._file.path, 'r') as file:
                data = json.load(file)
                from models.base_model import BaseModel

                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    if cls_name == 'BaseModel':
                        cls = BaseModel
                    else:
                        globals()[cls_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
