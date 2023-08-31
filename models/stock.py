#!/usr/bin/python3

"""
    Module: stock
    stock class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Enum, String, select
from sqlalchemy.orm import relationship
from sqlalchemy.sql import text

class Stock(BaseModel, Base):
    """ Class represents the each individual stock in the stock exchange """
    __tablename__ = "stocks"

    ticker = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    sector = Column(String(128), nullable=False)
    status = Column(Enum("active", "delisted", "suspended", name="stock_status_enum"), default= "active", nullable=False)
    data = relationship("StockData", back_populates = "stock")

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

    @classmethod
    def get_stock_by_ticker(cls, ticker):
        """ fetches stock using name """
        stmt = select(cls).where(cls.ticker == ticker)
        stock = models.storage.query(stmt)
        
        if len(stock) == 0:
            return None
        return stock[0]    
