#!/usr/bin/python3

"""
    Module: stock_data
    StockData class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Numeric



class StockData(BaseModel, Base):
    """ 
        Class represents individual data points at given times
        Data points show market activity for the given stock at given time
    """
    __tablename__ = "stock_data"

    prev = Column(Integer, nullable=False)
    current = Column(Integer, nullable=False)
    price_change = Column(Integer, nullable=False)
    percentage_price_change = Column(Numeric(precision= 5, scale= 4), nullable=False)
    high = Column(Integer, nullable=False)
    low = Column(Integer, nullable=False)
    volume = Column(Integer, nullable=False)
    average = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)
    stock_id = Column(String(60), ForeignKey("stocks.id"), nullable=False)
    stock = relationship("Stock", back_populates = "data")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.prev = args[0]
            self.current = args[1]
            self.price_change = args[2]
            self.percentage_price_change = args[3]
            self.high = args[4]
            self.low = args[5]
            self.volume = args[6]
            self.average = args[7]
            self.time = args[8]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
