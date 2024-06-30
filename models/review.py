#!/usr/bin/python3
"""
Review Module for HBNB project
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a Review for the HBNB project.
    """
    
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a Review instance.
        """
        super().__init__(*args, **kwargs)
