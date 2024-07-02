#!/usr/bin/python3
"""This module defines a base class for
all models in hbnb clone"""

import os
import uuid
from datetime import datetime
import MySQLdb


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        self.save_to_db()

    def save_to_db(self):
        """Saves instance data to MySQL database"""
        db = MySQLdb.connect(host="localhost", user="your_username",
                             passwd="your_password", db="your_db")
        cursor = db.cursor()
        query = """
                INSERT INTO base_model (id, created_at, updated_at)
                VALUES (%s, %s, %s)
                """
        cursor.execute(query, (self.id, self.created_at, self.updated_at))
        db.commit()
        db.close()

    def to_dict(self):
        """Convert instance into dict format"""
        res = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value
        res['__class__'] = self.__class__.__name__
        return res
