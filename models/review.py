#!/usr/bin/python3
""" Review Module for HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review class to store review info """
    place_id = ""
    user_id = ""
    text = ""
