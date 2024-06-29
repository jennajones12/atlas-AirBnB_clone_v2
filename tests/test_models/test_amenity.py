#!/usr/bin/python3

import sys
import os
import unittest
from models import Amenity

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models import test_basemodel

amenity_instance = Amenity()

class TestAmenity(test_basemodel):
    """Unit tests for Amenity class."""

    def setUp(self):
        """Set up test environment."""
        super().setUp()
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """Test the type of Amenity's name attribute."""
        new_instance = self.value()
        self.assertEqual(type(new_instance.name), str)

if __name__ == '__main__':
    unittest.main()
