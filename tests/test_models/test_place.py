#!/usr/bin/python3
"""Module contains tests for place model """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Implement test functions"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Tests user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Tests name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Tests description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Tests city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """Tests number_bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """Tests max_guest attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """Tests price_by_night attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """Tests latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """Tests longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """Tests amenity_ids attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
