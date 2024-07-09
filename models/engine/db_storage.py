#!/usr/bin/python3
""" Database Storage module for the HBNB project """

import MySQLdb
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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
    __db = None
    __cursor = None

    def __init__(self):
        """Initialize the database storage engine"""
        self.reload()

    def all(self, cls=None):
        """Query all objects or objects of a specific class"""
        objects = {}
        if cls:
            self.__cursor.execute("SELECT * FROM {}"
                                  .format(cls.__tablename__))
            results = self.__cursor.fetchall()
            for row in results:
                key = "{}.{}".format(row[1], row[0])
                objects[key] = cls(**row)
        else:
            # Loop through registered classes and fetch objects
            for cls in classes.values():
                self.__cursor.execute("SELECT * FROM {}"
                                      .format(cls.__tablename__))
                results = self.__cursor.fetchall()
                for row in results:
                    # Create instances from retrieved rows and add to dict
                    key = "{}.{}".format(row[1], row[0])
                    objects[key] = cls(**row)
        return objects

    def new(self, obj):
        """Add object to the database"""
        values = ', '.join(["'{}'".format(val) for val in
                            obj.to_dict().values()])
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            obj.__tablename__,
            ', '.join(obj.to_dict().keys()),
            values
        )
        self.__cursor.execute(query)
        self.__db.commit()

    def save(self):
        """Commit changes to the database"""
        self.__db.commit()

    def delete(self, obj=None):
        """Delete object from the database"""
        if obj:
            query = "DELETE FROM {} WHERE id='{}'".format(
                obj.__tablename__, obj.id)
            self.__cursor.execute(query)
            self.__db.commit()

    def reload(self):
        """Reload data from the database by establishing a new connection"""
        self.__db = MySQLdb.connect(
            host='localhost',
            user='user',
            passwd='password',
            db='db_name',
            port=3306,
            charset="utf8"
        )
        self.__cursor = self.__db.cursor()

    def close(self):
        """Close database connection"""
        if self.__cursor:
            self.__cursor.close()
        if self.__db:
            self.__db.close()
