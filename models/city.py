#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, String
from models.base_model import BaseModel


class City(BaseModel):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
