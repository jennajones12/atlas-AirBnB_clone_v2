#!/usr/bin/python3

"""
State Module for HBNB project
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a State for the HBNB project.
    """
    
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a State instance.
        """
        super().__init__(*args, **kwargs)
