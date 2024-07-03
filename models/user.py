#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel


class User(BaseModel):
    """defines user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
