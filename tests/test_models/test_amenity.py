#!/usr/bin/python3
"""Test Amenity Module"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Setup method to initialize an instance before each test"""
        self.model = Amenity()

    def test_name_is_assigned(self):
        """Test that name is assigned"""
        self.assertEqual(type(self.model.name), str)


if __name__ == '__main__':
    unittest.main()
