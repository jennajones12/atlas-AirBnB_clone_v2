#!/usr/bin/python3
""" Unit Tests for the console """
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Tests the Console"""

    def test_all(self):
        """Tests all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual(f.getvalue(), "[]\n")

    def test_show(self):
    """Tests show"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("create User")
        user_id = f.getvalue().strip()
        f = StringIO()
        with patch('sys.stdout', new=f):
            HBNBCommand().onecmd(f"show User {user_id}")
            print(f.getvalue())
            self.assertTrue("User." + user_id in f.getvalue())

    def test_create(self):
    """Tests create"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("create User")
        output = f.getvalue().strip()
        self.assertRegex(output, r'^[\w-]+$', "Output should match UUID format")
   
    def test_update(self):
    """Tests update"""
    with patch('sys.stdout', new=StringIO()) as f:
        HBNBCommand().onecmd("create User")
        user_id = f.getvalue().strip()
        f = StringIO()
        with patch('sys.stdout', new=f):
            HBNBCommand().onecmd(f"update User {user_id} first_name \"John\"")
            HBNBCommand().onecmd(f"show User {user_id}")
            print(f.getvalue())
            self.assertTrue("\"first_name\": \"John\"" in f.getvalue())

    def test_destroy(self):
        """Tests destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            f = StringIO()
            with patch('sys.stdout', new=f):
                HBNBCommand().onecmd(f"destroy User {user_id}")
                HBNBCommand().onecmd("all User")
                self.assertFalse("User." + user_id in f.getvalue())


if __name__ == "__main__":
    unittest.main()
