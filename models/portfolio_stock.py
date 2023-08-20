#!/usr/bin/python3

"""
    Module: portfolio_stock
    PortfolioStock class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey, String


class PortfolioStock(BaseModel, Base):
    """ 
        Class represents a stock in aportfolio

    """
    __tablename__ = "portfolio_stocks"

    quantity = Column(Integer, nullable=False)
    portfolio_id = Column(String(60), ForeignKey('portfolios.id'), primary_key=True, nullable=False)
    stock_id = Column(String(60), ForeignKey('stocks.id'), primary_key=True, nullable=False)

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            self.quantity = args[0]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
