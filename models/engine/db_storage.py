#!/usr/bin/python3
""" Database Storage module for the HBNB project """

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """ class manages storage of hbnb models in a SQL database """
    __engine = None
    __session = None

    def __init__(self):
        """ initializes DBStorage """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns a dictionary of models currently in storage """
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
            else:
                classes = [State, City]
                for cls in classes:
                    objs = self.__session.query(cls).all()
                    for obj in objs:
                        key = obj.__class__.__name__ + '.' + obj.id
                        new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """ adds new obj to database session """
        self.__session.add(obj)

    def save(self):
        """ commits changes of current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes obj from current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reloads data from database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
