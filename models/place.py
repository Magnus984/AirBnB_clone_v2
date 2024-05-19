#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import os
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
        "place_amenity", Base.metadata,
        Column(
            'place_id', String(60),
            ForeignKey('places.id'), primary_key=True,
            nullable=False
            ),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'), primary_key=True,
            nullable=False
            )
        )


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
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            viewonly=False, back_populates="places"
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

        @property
        def amenities(self):
            amenities_instances = []
            from models import storage
            for k, v in storage.all(Amenity).items():
                if v["amenity.id"] in self.amenity_ids:
                    amenities_instances.append({k, v})
            return amenities_instances

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
