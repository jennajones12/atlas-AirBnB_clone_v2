#!/usr/bin/python3

"""
User Module for HBNB project
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User for the HBNB project.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a User instance.
        """
        super().__init__(*args, **kwargs)
