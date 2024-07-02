#!/usr/bin/python3
"""Test BaseModel Module"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Setup method to initialize an instance before each test"""
        self.model = BaseModel()

    def test_id_is_assigned(self):
        """Test that an id is assigned"""
        self.assertIsNotNone(self.model.id)

    def test_created_at_is_assigned(self):
        """Test that created_at is assigned"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_assigned(self):
        """Test that updated_at is assigned"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_save_updates_updated_at(self):
        """Test that save updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)


if __name__ == '__main__':
    unittest.main()
