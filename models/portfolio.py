#!/usr/bin/python3

"""
    Module: portfolio
    Portfolio class
"""

from models.base_model import BaseModel, Base
import models
from models.portfolio_stock import PortfolioStock
from models.stock import Stock
from sqlalchemy import Column, ForeignKey, String, select
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

    def portfolio_stocks_valuation(self, stock_data):
        """calculates the current market value of stocks in the portfolio"""

        statement = select(PortfolioStock.quantity, Stock.ticker).join(
            PortfolioStock.stock).where(PortfolioStock.portfolio_id == self.id)
        valuation = 0
        data = models.storage.execute(statement)
        for st_data in stock_data:
            ticker = st_data.get("ticker")
            for dt in data:
                if ticker == dt.get("ticker"):
                    valuation += (dt.get("quantity") * st_data.get("price"))
        return valuation
