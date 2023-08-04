#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import uuid


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    def __init__(self):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

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
