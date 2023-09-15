#!/usr/bin/python3

"""
    Module: transaction
    Transaction class
"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Transaction(BaseModel, Base):
    """ 
        Class represents a transactio carried out by user on given  portfolio

    """
    __tablename__ = "transactions"

    item = Column(String(60), nullable=False)
    item_id = Column(String(60), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    transaction_type = Column(Enum("buy", "sell", name= "transation_type_enum"), nullable=False)
    total = Column(Integer, nullable=False)
    portfolio_id = Column(String(60), ForeignKey("portfolios.id"), nullable=False)
    portfolio = relationship("Portfolio", back_populates="transactions")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            self.item = args[0]
            self.item_id = args[1]
            self.price = args[2]
            self.quantity = args[3]
            self.transaction_type = args[4]
            self.total = args[5]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
