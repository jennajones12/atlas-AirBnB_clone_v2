#!/usr/bin/python3
""" file storage class for AirBnB """
import json


class FileStorage:
    """ manages storage of hbnb models in JSON format """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ returns dict of models currently in storage """
        if cls:
            return {key: obj for key, obj in self.__objects.items()
                    if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """ adds new obj to storage dict """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """ saves storage dict to file """
        temp = {}
        for key in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    # noinspection PyUnresolvedReferences
    def reload(self):
        """ loads storage dict from file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ deletes obj from __objects if it's inside """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
