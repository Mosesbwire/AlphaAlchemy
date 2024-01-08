#!/usr/bin/python3

"""
    Module: base_model
    Contains the BaseModel class
"""

from datetime import datetime, timezone
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()


class BaseModel:
    """ BaseModel class which provides a blueprint that other models will inherit from """

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(
        timezone.utc), nullable=False)

    def __init__(self):
        """ constructor function """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def update(self):
        models.storage.save()

    def __str__(self):
        """ returns string representation of the object when printed """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """ converts instance attributes to a dict """
        date_format = "%Y-%m-%d %H:%M:%S.%f"
        instance_dict = self.__dict__

        created_at = self.created_at
        updated_at = self.updated_at

        instance_dict["created_at"] = created_at.strftime(date_format)
        instance_dict["updated_at"] = updated_at.strftime(date_format)
        instance_dict.pop("password", None)

        instance_dict = {key: val for (
            key, val) in instance_dict.items() if key != "_sa_instance_state"}

        return instance_dict
