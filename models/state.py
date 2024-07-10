#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """State class representing states in a database."""
    __tablename__ = 'states'

    if storage_type == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """getter attribute that returns list of City instances"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
