#!/usr/bin/python3

"""
Test suite for the BaseModel class in the models.base_model module
"""

import unittest
from datetime import datetime
import sys
import os

# Adjust the path to import from the root of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """
        Set up the test environment
        """
        self.model = BaseModel()

    def test_id_type(self):
        """
        Test that id is a string
        """
        self.assertEqual(type(self.model.id), str)

    def test_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_save_updates_updated_at(self):
        """
        Test that save updates the updated_at attribute
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_type(self):
        """
        Test that to_dict returns a dictionary
        """
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)

    def test_to_dict_format(self):
        """
        Test the keys in the to_dict output
        """
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        model_dict = self.model.to_dict()
        self.assertTrue(all(key in model_dict for key in expected_keys))

    def test_kwargs_initialization(self):
        """
        Test initialization with kwargs
        """
        kwargs_model = BaseModel(id="123", created_at=datetime.now(),
                                 updated_at=datetime.now())
        self.assertEqual(kwargs_model.id, "123")
        self.assertEqual(type(kwargs_model.created_at), datetime)
        self.assertEqual(type(kwargs_model.updated_at), datetime)

    def test_str_representation(self):
        """
        Test __str__ method
        """
        string = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)


if __name__ == "__main__":
    unittest.main()
