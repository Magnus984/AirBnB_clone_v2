#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    __table_args__ = {'mysql_charset': 'latin1'}
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        state_id = Column(
                String(60), ForeignKey('states.id'), nullable=False
                )
        name = Column(String(128), nullable=False)
        state = relationship("State")
        places = relationship(
                "Place", back_populates="cities",
                cascade="all, delete, delete-orphan"
                )
    else:
        state_id = ''
        name = ''
