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
        with self.patched_stdout:
            self.console.onecmd("create BaseModel")
            is_instance = isinstance(
                storage.all()["BaseModel." +
                                self.mock_stdout.getvalue().strip()],
                                    BaseModel
            )
            self.assertTrue(is_instance)

    def test_show(self):
        """Test show command functionality."""
        with self.patched_stdout:
            self.hbnb.onecmd("create BaseModel")
            self.hbnb.onecmd("show BaseModel "
                             + self.mock_stdout.getvalue().strip())
            self.assertTrue(
                self.mock_stdout.getvalue()
                .strip() != "** no instance found **"
            )


if __name__ == "__main__":
    unittest.main()
