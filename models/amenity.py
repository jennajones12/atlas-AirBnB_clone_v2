#!/usr/bin/python3
"""
Amenity Module for HBNB project
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity for the HBNB project.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes an Amenity instance.
        """
        super().__init__(*args, **kwargs)
