import unittest
from datetime import datetime
from models.base_model import BaseModel

class test_basemodel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_kwargs(self):
        """Test initialization with kwargs."""
        copy = {
            'id': '1234', 
            'created_at': '2023-07-01T12:00:00.000000',
            'updated_at': '2023-07-01T12:00:00.000000', 
            'name': 'San Francisco'
        }
        new = BaseModel(**copy)
        self.assertEqual(new.name, 'San Francisco')

    def test_updated_at(self):
        """Test updated_at attribute."""
        n = {
            'id': '1234', 
            'created_at': '2023-07-01T12:00:00.000000',
            'updated_at': '2023-07-01T12:00:00.000000'
        }
        new = BaseModel(**n)
        self.assertEqual(
            new.updated_at, 
            datetime.strptime(
                '2023-07-01T12:00:00.000000', 
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        )

    def test_kwargs_one(self):
        """Test that unexpected keys raise KeyError."""
        n = {
            'id': '1234', 
            'created_at': '2023-07-01T12:00:00.000000',
            'updated_at': '2023-07-01T12:00:00.000000', 
            'unexpected_key': 'unexpected_value'
        }
        with self.assertRaises(KeyError):
            BaseModel(**n)

if __name__ == "__main__":
    unittest.main()
