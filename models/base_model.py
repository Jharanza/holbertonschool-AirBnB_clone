#!/usr/bin/python3
<<<<<<< HEAD
''' Module base for the files of the proyect '''
=======
"""
Contains class BaseModel
"""

>>>>>>> 163857a830757f250c5c92b59dfd20197caddfa1
from datetime import datetime
import uuid


class BaseModel:
<<<<<<< HEAD
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
=======
    """The BaseModel class from which future classes will be derived"""
    def __init__(self):
        """Initialization of the base model"""
>>>>>>> 163857a830757f250c5c92b59dfd20197caddfa1
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

<<<<<<< HEAD
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
=======
    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the atribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance"""
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] =self.__class__.__name__
        return new_dict 
>>>>>>> 163857a830757f250c5c92b59dfd20197caddfa1
