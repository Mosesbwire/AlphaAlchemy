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
from utils.currency.conversion import to_cents, to_unit_currency


class StockData(BaseModel, Base):
    """ 
        Class represents individual data points at given times
        Data points show market activity for the given stock at given time
    """
    __tablename__ = "stock_data"

    price = Column(Integer, nullable=False)
    volume = Column(String(60), nullable=False)
    stock_id = Column(String(60), ForeignKey("stocks.id"), nullable=False)
    stock = relationship("Stock", back_populates="data")

    def __init__(self, current_price: float, vol: int):
        """ class constructor """
        super().__init__()
        self._price = None
        self._volume = None
        self.price = current_price
        self.volume = vol

    @property
    def price(self):
        return to_unit_currency(self._price)

    @price.setter
    def price(self, price):
        if (price < 0):
            raise ValueError("Price cannot be less than zero.")
        self._price = to_cents(price)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, vol):
        if (vol < 0):
            raise ValueError("Volume traded cannot be less than zero")
        self._volume = vol
