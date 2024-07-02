# models/engine/file_storage.py

import json
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file, default=str)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = models.classes[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
