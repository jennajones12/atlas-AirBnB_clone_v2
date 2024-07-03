#!/usr/bin/python3
"""Unit tests for HBNB console commands"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test case."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up after the test case."""
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command functionality."""
        self.console.onecmd("create BaseModel")
        print(storage.all())
        is_instance = isinstance(
            storage.all()["BaseModel." + mock_stdout.getvalue().strip()],
            BaseModel
        )
        self.assertTrue(is_instance)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command functionality."""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("show BaseModel " + mock_stdout.getvalue().strip())
        self.assertTrue(
            mock_stdout.getvalue().strip() != "** no instance found **"
        )


if __name__ == "__main__":
    unittest.main()
