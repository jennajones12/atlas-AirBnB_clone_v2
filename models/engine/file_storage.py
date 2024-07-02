#!/usr/bin/python3
"""
This module defines the FileStorage class responsible for serializing
instances to JSON and deserializing JSON back to instances.
"""
import json
from models.base_model import BaseModel
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    """ Custom JSON Encoder for datetime objects """

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


class FileStorage:
    """
    Handles serialization and deserialization of instances to/from JSON
    stored in a file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file __file_path """
        json_data = {}
        for key, value in FileStorage.__objects.items():
            json_data[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w',
                  encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file, cls=DateTimeEncoder)

    def reload(self):
        """ Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as file:
                json_data = json.load(file)
                for key, value in json_data.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
