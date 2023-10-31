#!/usr/bin/python3

"""
    Module: portfolio
    Portfolio class
"""

from models.base_model import BaseModel, Base
import models
from models.portfolio_stock import PortfolioStock
from models.stock import Stock
from models.transaction import Transaction
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

    __LOT_SIZE = 100

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
                if ticker == dt.ticker:
                    valuation += (dt.quantity * st_data.get("price"))
        return valuation

    def valid_lot_size(self, qty):
        return qty % self.__LOT_SIZE == 0

    def create_order_transaction(self, stock: Stock, price: float, quantity: int, transaction_type: str):
        try:
            transaction = Transaction(
                stock.stock_ticker, stock.id, price, quantity, transaction_type)
            return transaction.create(self)
        except ValueError as e:
            return None

    def add_stock(self, stock: Stock, quantity: int, portfolio_stock=None):
        if portfolio_stock:
            qty = portfolio_stock.stock_quantity + quantity
            portfolio_stock.stock_quantity = qty
            return portfolio_stock
        try:
            ps = PortfolioStock(quantity, stock, self)
            return ps.create()
        except ValueError as e:
            return None

    def buy_stock(self, bid_price: float, quantity: int, stock: Stock):
        """ carry out action to buy stocks"""
        transaction_type = "buy"
        stmt = select(PortfolioStock).where(
            PortfolioStock.stock_id == stock.id)

        if not self.valid_lot_size(quantity):
            raise ValueError(
                "Transaction quantity must be in multiples of 100")

        portfolio_stock = models.storage.query(stmt)

        ps = None
        if portfolio_stock:

            ps = self.add_stock(stock, quantity, portfolio_stock[0])
        else:
            ps = self.add_stock(stock, quantity)

        if not ps:
            return None

        order = self.create_order_transaction(
            stock, bid_price, quantity, transaction_type)

        if not order:
            return None

        return self
