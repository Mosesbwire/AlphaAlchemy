#!/usr/bin/python3

"""
    Module: user
    user class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ Class represents the User """
    __tablename__ = "users"

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    portfolios = relationship("Portfolio", back_populates = "user",
            cascade = "all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.first_name = args[0]
            self.last_name = args[1]
            self.email = args[2]
            self.password = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
