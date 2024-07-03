#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.city import City


class State(BaseModel):
    """ state class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    city_relation = relationship('City', cascade="all, delete", backref='state')

    @property
    def cities(self):
        """getter attribute that returns list of City instances"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
