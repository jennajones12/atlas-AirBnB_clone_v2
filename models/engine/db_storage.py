#!/usr/bin/python3
""" Database Storage module for the HBNB project """

import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}

username = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db_name = getenv('HBNB_MYSQL_DB')
connection = f'mysql+mysqldb://{username}:{password}@{host}/{db_name}'


class DBStorage:
    """Database storage engine for HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine"""
        self.__engine = create_engine(connection, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        objs = {}
        if cls:
            results = self.__session.query(cls).all()
            for obj in results:
                key = f"{cls.__name__}.{obj.id}"
                objs[key] = obj
        else:
            for class_name in classes.values():
                results = self.__session.query(class_name).all()
                for obj in results:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Add object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """Close the session"""
        self.__session.close()


storage = DBStorage()
