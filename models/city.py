#!/usr/bin/python3
"""City Module for HBNB project"""
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """City class representing cities in a database."""
    __tablename__ = 'cities'

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize City object."""
        super().__init__(*args, **kwargs)
