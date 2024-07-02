#!/usr/bin/python3
"""Database Storage module for the HBNB project"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base

class DBStorage:
    """Database storage engine for HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine"""
        self.__engine = create_engine('mysql+mysqldb://user:password@localhost/db_name')

    def all(self, cls=None):
        """Query on the current database session"""
        # Implementation of the all method

    def new(self, obj):
        """Add the object to the current database session"""
        # Implementation of the new method

    def save(self):
        """Commit all changes of the current database session"""
        # Implementation of the save method

    def delete(self, obj=None):
        """Delete from the current database session"""
        # Implementation of the delete method

    def reload(self):
        """Reloads the database"""
        # Implementation of the reload method
