#!/usr/bin/python3

"""
Amenity Module for HBNB project
"""

from models.base_model import BaseModel


class Amenity:
    def __init__(self, id=None, name=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """ Returns a dictionary representation of the Amenity instance """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat()
            if self.created_at else None,
            'updated_at': self.updated_at.isoformat()
            if self.updated_at else None
        }
