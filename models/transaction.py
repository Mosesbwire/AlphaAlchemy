#!/usr/bin/python3

"""
    Module: transaction
    Transaction class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Transaction(BaseModel):
    """ 
        Class represents a transactio carried out by user on given  portfolio

    """
    __tablename__ = "transactions"

    item = Column(String(60), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    transaction_type = Column(String(60), nullable=False)
    total = Column(Integer, nullbale=False)
    portfolio_id = Column(String(60), ForeignKey("portfolios.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            self.item = args[0]
            self.price = args[1]
            self.quantity = args[2]
            self.transaction_type = args[3]
            self.total = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
