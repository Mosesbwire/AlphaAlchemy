#!/usr/bin/python3

"""
    Module: portfolio_stock
    PortfolioStock class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class PortfolioStock(BaseModel, Base):
    """ 
        Class represents a stock in aportfolio

    """
    __tablename__ = "portfolio_stocks"

    quantity = Column(Integer, nullable=False)
    portfolio_id = Column(String(60), ForeignKey(
        'portfolios.id'), primary_key=True, nullable=False)
    stock_id = Column(String(60), ForeignKey('stocks.id'),
                      primary_key=True, nullable=False)
    stock = relationship("Stock")

    def __init__(self, quantity: int, stock, portfolio):
        """ class constructor """
        super().__init__()
        self.quantity = quantity
        self.stock = stock
        self._portfolio = portfolio

    @property
    def stock_quantity(self):
        return self.quantity

    @stock_quantity.setter
    def stock_quantity(self, qty):
        if qty < 0:
            raise ValueError("Quantity cannot be less than zero")
        self.quantity = qty

    def create(self):
        self._portfolio.stocks.append(self)
        return self
