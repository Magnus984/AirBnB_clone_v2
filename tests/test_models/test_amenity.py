#!/usr/bin/python3
"""Module contains tests for model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Implements test functions for model"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name(self):
        """Tests name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
