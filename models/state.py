#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        from sqlalchemy.orm import relationship
        cities = relationship(
                "City", back_populates="state",
                cascade="all, delete, delete-orphan",
                )
    else:
        @property
        def cities(self):
            city_instances = []
            from models import storage
            for key, value in storage.all(City).items():
                if value["state_id"] == self.id:
                    city_instances.append({key: value})
            return city_instances
