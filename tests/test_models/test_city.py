#!/usr/bin/python3
"""
Module contains tests for city model
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Implements test functions for city model"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Verifies state_id attribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Verifies name of city model"""
        new = self.value()
        self.assertEqual(type(new.name), str)
