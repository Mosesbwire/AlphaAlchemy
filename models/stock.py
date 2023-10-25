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
    status = Column(Enum("active", "delisted", "suspended",
                    name="stock_status_enum"), default="active", nullable=False)
    data = relationship("StockData", back_populates="stock")

    __stock_status = {
        "ACTIVE": "active",
        "DELISTED": "delisted",
        "SUSPENDED": "suspended"
    }

    def __init__(self, stock_ticker: str, stock_name: str, stock_sector: str, stock_status: str = __stock_status["ACTIVE"]):
        """ class constructor """
        super().__init__()

        self._ticker = None
        self._name = None
        self._sector = None
        self._status = None
        self.ticker = stock_ticker
        self.name = stock_name
        self.sector = stock_sector
        self.status = stock_status

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        if len(ticker) > 6:
            raise ValueError("Ticker symbol cannot be more than 6 characters")
        self._ticker = ticker.upper()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, sec):
        self._sector = sec

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status not in self.__stock_status:
            raise ValueError("Invalid status type")
        self._status = self.__stock_status[status]

    @classmethod
    def get_stock_by_ticker(cls, ticker):
        """ fetches stock using ticker symbol """
        stmt = select(cls).where(cls.ticker == ticker)
        stock = models.storage.query(stmt)

        if len(stock) == 0:
            return None
        return stock[0]
