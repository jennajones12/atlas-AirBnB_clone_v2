#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from tests.test_models.test_base_model import test_basemodel


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = self.get_city_class()

    def get_city_class(self):
        from models.city import City
        return City

    def test_state_id(self):
        """Test state_id attribute type."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute type."""
        new = self.value()
        self.assertEqual(type(new.name), str)

if __name__ == "__main__":
    unittest.main()
