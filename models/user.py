#!/usr/bin/python3
""" User Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ User class """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', cascade="all, delete", backref='user')

    def __init__(self, *args, **kwargs):
        """Initialize User object."""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
