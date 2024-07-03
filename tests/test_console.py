#!/usr/bin/python3
"""Unit tests for HBNB console commands"""
import unittest
from unittest.mock import patch
import pycodestyle
import os

# Import all test classes from individual test files
from tests.test_models.test_amenity import TestAmenity
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_city import TestCity, test_City, Test_PEP8
from tests.test_models.test_place import test_Place
from tests.test_models.test_review import test_review
from tests.test_models.test_state import test_state
from tests.test_models.test_user import test_User

if __name__ == "__main__":
    unittest.main()
