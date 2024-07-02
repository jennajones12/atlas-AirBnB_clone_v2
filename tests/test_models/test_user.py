#!/usr/bin/python3

"""
User Module for HBNB project
"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def __str__(self):
        """Return str rep of User instance."""
        return "[User] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        """Return dict rep of User instance."""
        dict_copy = self.__dict__.copy()
        dict_copy.update({
            "__class__": type(self).__name__,
        })
        return dict_copy
