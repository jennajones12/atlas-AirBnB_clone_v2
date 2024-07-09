#!/usr/bin/python3
""" Database Storage module for the HBNB project """

import models
from models.base_model import BaseModel, Base
from models import User, State, City, Amenity, Place, Review
from os import getenv
from sqlalchemy import create_engine, exc
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

    def __init__(self)
    """Initialize the database storage engine"""
    pass

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        objs = {}
        if cls:
            results = self.__session.query(cls).all()
            for obj in results:
                key = f"{cls.__name__}.{obj.id}"
                objs[key] = obj
        else:
            for class_ in classes:
                results = self.__session.query(class ).all()
                for obj in results:
                    key = f"{class_.__name__}.{obj.id}"
                    objs[key] = obj
        return objects

    def new(self, obj):
        """Add object to the database"""
        if obj not in self.__session:
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the database"""
        split_key = key.split(".")
        class_name = split_key[0]
        obj_id = split_key[1]
        obj = {}
        if class_name not in classes:
            return
        for o in self.all(class_name).items():
            if o[1].id == obj_id:
                obj = o[1]
                break
        if obj is None:
            print(" ** object not found to delete ** ")
            return
        self.__session.delete(obj)
        print(f"Deleted {key}")

    def reload(self):
        """Reload data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the session"""
        self.__session.remove()


storage = DBStorage()
