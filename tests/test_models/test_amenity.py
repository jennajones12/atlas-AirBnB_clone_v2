#!/usr/bin/python3

"""
Test suite for the Amenity class in the models.amenity module
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_amenity(test_basemodel):
    """
    Test cases for the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test case for Amenity
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """
        Test that name is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
