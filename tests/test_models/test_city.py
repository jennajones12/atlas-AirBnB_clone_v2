#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
import os
import pycodestyle
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test state_id attribute type."""
        new = self.value(state_id="CA")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Test name attribute type."""
        new = self.value(name="San Francisco")
        self.assertEqual(type(new.name), str)


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """Tests for the City class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests."""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Clean up after the tests."""
        del cls.city

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Test that city.py conforms to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """Check for docstrings in City."""
        self.assertIsNotNone(City.__doc__)

    def test_save_City(self):
        """Test save method."""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """Test to_dict method."""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()

