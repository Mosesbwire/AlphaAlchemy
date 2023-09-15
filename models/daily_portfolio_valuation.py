#!/usr/bin/python3

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, ForeignKey, BigInteger, String, DateTime
from sqlalchemy.orm import relationship

class DailyPortfolioValuation(BaseModel, Base):
    """
        class represent the market value of porfolio at close of business
    """
    __tablename__ = "daily_portfolio_valuations"

    portfolio_id = Column(String(60), ForeignKey("portfolios.id"), nullable=False)
    portfolio_value = Column(BigInteger, nullable=False)
    portfolio = relationship("Portfolio", back_populates= "valuations")

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            
            self.portfolio_value = args[0]
            
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
