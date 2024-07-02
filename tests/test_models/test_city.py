#!/usr/bin/python3
"""Test City Module"""
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Test cases for the City class"""

    def setUp(self):
        """Setup method to initialize an instance before each test"""
        self.model = City()
        self.model.name = "San Francisco"
        self.model.state_id = "CA"

    def test_name_is_assigned(self):
        """Test that name is assigned"""
        self.assertEqual(type(self.model.name), str)

    def test_state_id_is_assigned(self):
        """Test that state_id is assigned"""
        self.assertEqual(type(self.model.state_id), str)


if __name__ == '__main__':
    unittest.main()
