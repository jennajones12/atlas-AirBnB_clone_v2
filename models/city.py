#!/usr/bin/python3
"""
City Module for HBNB project
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City for the HBNB project.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes City instance.
        """
        super().__init__(*args, **kwargs)
