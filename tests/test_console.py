#!/usr/bin/python3
"""Unit tests for HBNB console commands"""
import unittest
from unittest.mock import patch
import pycodestyle
import os

# Import all test classes from individual test files
from tests.test_models.test_amenity import Amenity
from tests.test_models.test_base_model import BaseModel
from tests.test_models.test_city import City
from tests.test_models.test_place import Place
from tests.test_models.test_review import Review
from tests.test_models.test_state import State
from tests.test_models.test_user import User

if __name__ == "__main__":
    unittest.main()
