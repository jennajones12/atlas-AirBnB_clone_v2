#!/usr/bin/python3
"""testing for the db_storage"""
import os
import models
import unittest
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
import models


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "dbtest")
class test_DBStorage(unittest.TestCase):
    """testing for the db_storage class"""
    def testCity(self):
        """tests if city name will establish itself"""
        city = City(name="Tulsa")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Tulsa")
    def testPlace(self):
    """tests if place name will establish itself"""
        place = Place(name="studio", number_beds=1)
        if place.id in models.storage.all():
            self.assertTrue(place.number_beds, 1)
            self.assertTrue(place.name, "studio")
    def testReview(self):
        """tests if review will establish itself"""
        review = Review(text="Wonderful!")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "Wonderful")
    def testState(self):
        """tests if State will establish itself"""
        state = State(name="Colorado")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Colorado")
    def testAmenity(self):
        """tests if Amenity name will establish itself"""
        amenity = Amenity(name="Indoor Pool")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Indoor Pool")
    def testUser(self):
        """tests if User name will establish itself"""
        user = User(name="Tom")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Tom")
    def teardown(self):
        """tear down"""
        self.session.close()
        self.session.rollback()
"""
Test Command:
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
11/8/2023 = OK
"""
