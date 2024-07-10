#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """City class representing cities in a database."""
    __tablename__ = 'cities'
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
