#!/usr/bin/python3

"""
    Module: user
    user class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import BigInteger, Column, String, select
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ Class represents the User """
    __tablename__ = "users"

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    balance = Column(BigInteger, default = 5000000, nullable = False)
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
            self.balance = 5000000
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    @classmethod
    def get_portfolios(cls, user_id):
        stmt = select(cls).where(cls.id == user_id)

        data = models.storage.query(stmt)
        user = data[0]
        return user.portfolios

    @classmethod
    def get_user_by_email(cls, email):
        stmt = select(cls).where(cls.email == email)

        user = models.storage.query(stmt)

        if len(user) > 0:
            return user[0]
        
        return None
