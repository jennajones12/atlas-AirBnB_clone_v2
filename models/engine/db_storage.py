#!/usr/bin/python3
""" Database Storage module for the HBNB project """

import models
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from models.place import Place
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

        try:
            if cls:
                # Query objects of a specific class
                results = self.__session.query(cls).all()
                for obj in results:
                    key = f"{cls.__name__}.{obj.id}"
                    objs[key] = obj
            else:
                # Query all objects if cls is not provided
                for class_name in classes.values():
                    results = self.__session.query(class_name).all()
                    for obj in results:
                        key = f"{obj.__class__.__name__}.{obj.id}"
                        objs[key] = obj

        except Exception as e:
            print(f"Error in DB query: {e}")
            objs = {}

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
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def link_amenity(self, amenity_id, place_id):
        """ Add an amenity to a place """
        from models.place import Place
        from models.amenity import Amenity

        place = amenity = None
        place = self.all('Place')['Place.' + place_id]
        amenity = self.all('Amenity')['Amenity.' + amenity_id]

        if place is None:
            print(" ** Place not found ** ")
            return False
        if amenity is None:
            print(" ** Amenity not found ** ")
            return False

        if place and amenity:
            place.amenities.append(amenity)
            self.__session.add(place)
            try:
                self.__session.commit()
                print(" ** Amenity and Place linked ** ")
                return True

            except exc.IntegrityError as e:
                if 'Duplicate entry' in str(e.orig):
                    print(" ** Amenity and Place already linked ** ")
                else:
                    print(e)
                self.__session.rollback()

                return False

            except Exception as e:
                print(e)
                self.__session.rollback()
                return False

    def unlink_amenity(self, amenity_id, place_id):
        """ Remove an amenity from a place """
        from models.place import Place
        from models.amenity import Amenity

        place = amenity = None
        place = self.all('Place')['Place.' + place_id]
        amenity = self.all('Amenity')['Amenity.' + amenity_id]

        if place is None:
            print(" ** Place not found ** ")
            return False
        if amenity is None:
            print(" ** Amenity not found ** ")
            return False

        if place and amenity:
            if amenity in place.amenities:
                place.amenities.remove(amenity)
                self.__session.add(place)
                try:
                    self.__session.commit()
                    print(" ** Amenity and Place unlinked ** ")
                    return True
                # Handle MySQLdb._exceptions.IntegrityError here

                except self.__engine._exceptions.IntegrityError as e:
                    print(e[1])
                    self.__session.rollback()
                    return False
                except Exception as e:
                    print(e)
                    self.__session.rollback()
                    return False
            else:
                print(" ** Amenity and Place not linked ** ")
                return False

    def close(self):
        """Close the session"""
        self.__session.remove()


storage = DBStorage()
