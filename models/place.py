#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float  # Import Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Place class representing places in a database."""
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)  # Now Float is defined
    longitude = Column(Float)
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
