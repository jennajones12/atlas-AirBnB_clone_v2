#!/usr/bin/python3

"""Amenity Module for HBNB project"""

from datetime import datetime
import models  # Assuming models is the storage package

class BaseModel:
    """Base model for other classes to inherit from."""
    
    def __init__(self):
        self.__id = ""
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        d = self.__dict__.copy()
        if "_BaseModel__updated_at" in d:
            del d["_BaseModel__updated_at"]
        return d

    def save(self):
        """Update updated_at and save the data using storage package."""
        self.updated_at = datetime.now()
        models.storage.save()

    @property
    def id(self):
        """Getter for id."""
        return self.__id

    @id.setter
    def id(self, value):
        """Setter for id."""
        self.__id = value

    @property
    def updated_at(self):
        """Getter for updated_at."""
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at."""
        self.__updated_at = value

    @property
    def created_at(self):
        """Getter for created_at."""
        return self.__created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at."""
        self.__created_at = value
