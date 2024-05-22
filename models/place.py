#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
import os
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    __table_args__ = {'mysql_charset': 'latin1'}
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
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
        reviews = relationship(
                "Review", back_populates="place",
                cascade="all, delete, delete-orphan"
                )
        amenities = relationship(
            "Amenity", secondary="place_amenity",
            viewonly=False, back_populates="place_amenities"
            )

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
                ),
                **{'mysql_charset': 'latin1'}
            )
    else:
        city_id = ""
        user_id = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            review_instances = []
            from models import storage
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    review_instances.append(value)
            return review_instances

        @property
        def amenities(self):
            amenities_instances = []
            from models import storage
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_instances.append(value)
            return amenities_instances

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
