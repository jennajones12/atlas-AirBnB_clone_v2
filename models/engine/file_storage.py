#!/usr/bin/python3

"""
This module defines the FileStorage class responsible for serializing
instances to JSON and deserializing JSON back to instances.
"""

import json
from models.base_model import BaseModel


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
            # Refactored to adhere to line length limit
            json_data = {k: v.to_dict() for k, v in
                         FileStorage.__objects.items()}
            json.dump(json_data, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file exists;
        otherwise, do nothing)"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                FileStorage.__objects = {k: BaseModel(**v)
                                         for k, v in data.items()}
        except FileNotFoundError:
            pass
