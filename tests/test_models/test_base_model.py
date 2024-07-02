#!/usr/bin/python3
"""Unit tests for BaseModel class and related functionality."""
import unittest
import datetime
import json
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class."""

    def setUp(self):
        """Set up for tests."""
        pass

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation."""
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_kwargs(self):
        """Test instantiation with kwargs."""
        i = BaseModel()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertNotEqual(new, i)

    def test_kwargs_int(self):
        """Test instantiation with invalid kwargs."""
        i = BaseModel()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save method."""
        i = BaseModel()
        i.save()
        key = 'BaseModel.' + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method."""
        i = BaseModel()
        self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(
            i.id, i.__dict__))

    def test_todict(self):
        """Test to_dict method."""
        i = BaseModel()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instantiation with None as kwargs."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = BaseModel(**n)
    
    def test_kwargs_one(self):
    """Test instantiation with unexpected key in kwargs."""
    n = {'name': 'test'}
    new = BaseModel(**n)
    self.assertNotIn('name', new.__dict__)
    
    def test_id(self):
        """Test id attribute."""
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute."""
        new = BaseModel()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute."""
        new = BaseModel()
        old_updated_at = new.updated_at
        new.save()
        self.assertNotEqual(old_updated_at, new.updated_at)

if __name__ == '__main__':
    unittest.main()
