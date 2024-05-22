#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    __table_args__ = {'mysql_charset': 'latin1'}
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        from sqlalchemy.orm import relationship
        place_amenities = relationship(
                'Place', secondary="place_amenity",
                back_populates='amenities'
                )
    else:
        name = ""
