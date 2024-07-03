#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel):
    """ city class containing state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('state.state_id'), nullable=False)
    name = Column(String(128), nullable=False)
