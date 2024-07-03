import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """Manages storage of hbnb models in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns dict of models currently in storage"""
        if cls:
            return {key: obj for key, obj in self.__objects.items()
                    if isinstance(obj, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new obj to storage dict"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dict to file"""
        temp = {}
        for key, val in self.__objects.items():
            temp[key] = val.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dict from file"""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    if cls_name in classes:
                        self.__objects[key] = classes[cls_name](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
