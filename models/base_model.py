#!/usr/bin/python3
"""Make base module for other classes"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """This is the parent class/model"""

    def __init__(self, *args, **kwargs):
        """initialize the BaseModel"""
        if len(kwargs) > 0:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Display the string representation of the BaseModel class"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """update class"""
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        """convert object to a dictionary"""
        dc = self.__dict__.copy()
        dc['__class__'] = 'BaseModel'
        dc['created_at'] = dc['created_at'].isoformat()
        dc['updated_at'] = dc['updated_at'].isoformat()
        return dc
