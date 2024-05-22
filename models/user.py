#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    __table_args__ = {'mysql_charset': 'latin1'}
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        from sqlalchemy.orm import relationship
        places = relationship(
                "Place", back_populates="user",
                cascade="all, delete, delete-orphan"
                )
        reviews = relationship(
                "Review", back_populates="user",
                cascade="all, delete, delete-orphan"
                )
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
