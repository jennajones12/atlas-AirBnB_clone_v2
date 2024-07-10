#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel, Base, storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City  # Import the City class


class State(BaseModel, Base):
    """class representing states in a database."""
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """getter that returns list of City instances"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
