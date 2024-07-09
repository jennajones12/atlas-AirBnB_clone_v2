#!/usr/bin/python3
""" Database Storage module for the HBNB project """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

classes = {
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}


class DBStorage:
    """Database storage engine for HBNB project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(
                                          getenv('HBNB_MYSQL_USER'),
                                          getenv('HBNB_MYSQL_PWD'),
                                          getenv('HBNB_MYSQL_HOST'),
                                          getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        objects = {}
        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        else:
            for cls in classes.values():
                query = self.__session.query(cls).all()
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        return objects

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
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Close the session"""
        self.__session.remove()


storage = DBStorage()
