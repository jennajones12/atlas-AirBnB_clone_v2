#!/usr/bin/python3
"""BaseModel Module for HBNB project"""

from datetime import datetime
import models  # Assuming models is the storage package
import uuid


class BaseModel:
    """Base model for other classes to inherit from."""
    
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            self.__dict__.update(kwargs)

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = self.__class__.__name__
        return d

    def save(self):
        """Update updated_at and save the data using storage package."""
        self.updated_at = datetime.now()
        models.storage.new(self)
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
