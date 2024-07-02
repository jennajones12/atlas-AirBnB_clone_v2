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
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(FileStorage.__objects, file, cls=DateTimeEncoder)

    def reload(self):
        """Deserializes JSON file to __objects (only if the JSON file exists;
        otherwise, do nothing)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                FileStorage.__objects = {k: BaseModel(**v)
                                         for k, v in data.items()}
        except FileNotFoundError:
            pass
