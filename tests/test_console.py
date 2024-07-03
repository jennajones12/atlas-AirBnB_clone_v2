#!/usr/bin/python3
"""Unit tests for HBNB console commands"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test case."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after the test case."""
        pass

    def test_create(self):
        """Test create command functionality."""
        #
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertIn("new_instance_id", output)

    def test_show(self):
        """Test show command functionality."""
        #
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 123")
            output = f.getvalue().strip()
            self.assertIn("Object details", output)


if __name__ == "__main__":
    unittest.main()
