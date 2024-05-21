#!/usr/bin/python3
"""DBStorage engine Module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """Defines DBstorage"""

    __engine = None
    __session = None
    __models = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        """Creates database engine"""
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.getenv("HBNB_MYSQL_USER"),
                    os.getenv("HBNB_MYSQL_PWD"),
                    os.getenv("HBNB_MYSQL_HOST"),
                    os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True
                )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        myDict = {}
        if cls:
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                myDict[key] = obj
        else:
            for model in self.__models:
                for obj in self.__session.query(model):
                    key = obj.__class__.__name__ + '.' + obj.id
                    myDict[key] = obj
        return myDict

    def new(self, obj):
        """Adds obj to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current db session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all db tables and current db session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False,
                )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.close()
