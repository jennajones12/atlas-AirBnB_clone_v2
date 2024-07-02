#!/usr/bin/python3
"""file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        if cls:
            return {k: v for k, v in self.__objects.items()
                    if isintstance(v, cls)}
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: eval(v['__class__'])(**v)
                              for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass
