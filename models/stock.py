#!/usr/bin/python3

"""
    Module: stock
    stock class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship


class Stock(BaseModel, Base):
    """ Class represents the each individual stock in the stock exchange """
    __tablename__ = "stocks"

    ticker = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    sector = Column(String(128), nullable=False)
    status = Columns(Enum("active", "delisted", "suspended", name="stock_status_enum"), default= "active", nullable=False)
    portfolios = relationship("Portfolio", secondary= "portfolio_stocks", backref="stocks")
    data = relationship("StockData", backref="stocks")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.ticker = args[0]
            self.name = args[1]
            self.sector = args[2]
            self.status = "active"
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
