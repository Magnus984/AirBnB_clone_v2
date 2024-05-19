#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
import os
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False
            )
    user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False
            )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    from sqlalchemy.orm import relationship
    cities = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                "Review", back_populates="place",
                cascade="all, delete, delete-orphan"
                )
    else:
        @property
        def reviews(self):
            review_instances = []
            from models import storage
            for k, v in storage.all(Review).items():
                if v["place_id"] == self.Place.id:
                    review_instances.append({k, v})
            return review_instances
