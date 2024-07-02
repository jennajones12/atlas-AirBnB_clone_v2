#!/usr/bin/python3

"""
Amenity Module for HBNB project
"""

from models.base_model import BaseModel
from datetime import datetime
import models


class Amenity(BaseModel):
    """ Amenity class that inherits from BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initialization of Amenity instance """
        super().__init__(*args, **kwargs)
        self.name = ""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(
                        self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

    def to_dict(self):
        """ Returns a dictionary representation of the instance """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def save(self):
        """ Save the current instance to the storage """
        self.updated_at = datetime.now()
        models.storage.save()
