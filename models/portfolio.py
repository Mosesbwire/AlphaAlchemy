#!/usr/bin/python3

"""
    Module: portfolio
    Portfolio class
"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Portfolio(BaseModel, Base):
    """ 
        Class represents a users portfolio

    """
    __tablename__ = "portfolios"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="portfolios")
    stocks = relationship("PortfolioStock")
    transactions = relationship("Transaction", back_populates="portfolio",
                                cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

    def create(self, user):
        user.portfolios.append(self)
        return self
