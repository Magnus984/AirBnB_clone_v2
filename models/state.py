#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {'mysql_charset': 'latin1'}
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        from sqlalchemy.orm import relationship
        cities = relationship(
                "City", back_populates="state",
                cascade="all, delete, delete-orphan",
                )
    else:
        name = ""

        @property
        def cities(self):
            city_instances = []
            from models import storage
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    city_instances.append(value)
            return city_instances
