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

    ticker = Column(String(60), unique=True, nullable=False)
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

    def __init__(self, stock_ticker: str, stock_name: str, stock_sector: str, stock_status: str = "ACTIVE"):
        """ class constructor """
        super().__init__()
        self.stock_ticker = stock_ticker
        self.stock_name = stock_name
        self.stock_sector = stock_sector
        self.stock_status = stock_status

    @property
    def stock_ticker(self):
        return self.ticker

    @stock_ticker.setter
    def stock_ticker(self, ticker):
        if len(ticker) > 6:
            raise ValueError("Ticker symbol cannot be more than 6 characters")
        self.ticker = ticker.upper()

    @property
    def stock_name(self):
        return self.name

    @stock_name.setter
    def stock_name(self, name):
        self.name = name

    @property
    def stock_sector(self):
        return self.sector

    @stock_sector.setter
    def stock_sector(self, sec):
        self.sector = sec

    @property
    def stock_status(self):
        return self.status

    @stock_status.setter
    def stock_status(self, status):
        if status not in self.__stock_status:
            raise ValueError("Invalid status type")
        self.status = self.__stock_status[status]

    @classmethod
    def get_stock_by_ticker(cls, ticker):
        """ fetches stock using ticker symbol """
        stmt = select(cls).where(cls.ticker == ticker)
        stock = models.storage.query(stmt)

        if len(stock) == 0:
            return None
        return stock[0]
