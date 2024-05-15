#!/usr/bin/python3
"""Module that contains tests for state model """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Implements functions for testing state model """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests name attribute of state model """
        new = self.value()
        self.assertEqual(type(new.name), str)
