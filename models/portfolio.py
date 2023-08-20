#!/usr/bin/python3

"""
    Module: portfolio
    Portfolio class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, BigInteger, String
from sqlalchemy.orm import relationship


class Portfolio(BaseModel, Base):
    """ 
        Class represents a users portfolio

    """
    __tablename__ = "portfolios"

    name = Column(String(128), nullable=True)
    capital = Column(BigInteger, nullable=False, default = 0)
    status = Column(Enum("active", "inactive", name="portfolio_enum_status"), default= "active", nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    transactions = relationship("Transaction", backref="portfolio",
            cascade = "all, delete, delete-orphan")
    stocks = relationship("Stock", secondary="portfolio_stocks",  backref="portfolios",
            cascade = "save-update, merge, delete")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        self.status = "active"
        if args:
            self.name = args[0]
            self.capital = args[1]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
