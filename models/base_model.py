#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
            String(60), nullable=False,
            primary_key=True, unique=True,
            default=lambda: str(uuid.uuid4())
            )
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            try:
                kwargs['updated_at'] = datetime.fromisoformat(
                        kwargs['updated_at']
                        )
                kwargs['created_at'] = datetime.fromisoformat(
                        kwargs['created_at']
                        )
            except (KeyError, ValueError):
                kwargs["updated_at"] = kwargs["created_at"] = datetime.utcnow()

            kwargs.pop("__class__", None)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        str1 = "[{:s}] ({:s}) {}"
        myDict = self.__dict__.copy()
        del myDict['_sa_instance_state']
        return str1.format(
                self.__class__.__name__, self.id, myDict
                )

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes current instance from storage"""
        from models import storage
        storage.delete(self)
