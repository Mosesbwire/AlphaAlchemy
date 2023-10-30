#!/usr/bin/python3

"""
    Module: transaction
    Transaction class
"""

import models
from models.base_model import BaseModel, Base
from utils.currency.conversion import to_cents, to_unit_currency
import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Transaction(BaseModel, Base):
    """ 
        Class represents a transaction carried out by user on given  portfolio

    """
    __tablename__ = "transactions"

    item = Column(String(60), nullable=False)
    item_id = Column(String(60), nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    transaction_type = Column(
        Enum("buy", "sell", name="transation_type_enum"), nullable=False)
    total = Column(Integer, nullable=False)
    portfolio_id = Column(String(60), ForeignKey(
        "portfolios.id"), nullable=False)
    portfolio = relationship("Portfolio", back_populates="transactions")

    def __init__(self, item: str, price: float, quantity: int, transaction_type: str):
        """ class constructor """
        super().__init__()
        self.transaction_item = item
        self.item_price = price
        self.item_quantity = quantity
        self.type_transaction = transaction_type
        self.transaction_total = self.calculate_total()

    @property
    def transaction_item(self):
        return self.item

    @transaction_item.setter
    def transaction_item(self, item):
        self.item = item

    @property
    def item_price(self):
        return to_unit_currency(self.price)

    @item_price.setter
    def item_price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be zero or less than zero")
        try:
            self.price = to_cents(price)
        except ValueError:
            print("error occured")

    @property
    def item_quantity(self):
        return self.quantity

    @item_quantity.setter
    def item_quantity(self, qty):
        if qty <= 0:
            raise ValueError("Quantity cannot be zero or less than zero")
        self.quantity = qty

    @property
    def type_transaction(self):
        return self.transaction_type

    @type_transaction.setter
    def type_transaction(self, transaction):
        trs_types = ["buy", "sell"]
        if transaction not in trs_types:
            raise ValueError(
                f"{transaction} is not a valid transaction type. Valid transactions are buy and sell")
        self.transaction_type = transaction

    @property
    def transaction_total(self):
        return to_unit_currency(self.total)

    @transaction_total.setter
    def transaction_total(self, cost):
        self.total = cost

    def calculate_total(self):
        """calculate total cost of transaction"""
        total_cost = self.item_price * self.item_quantity
        return to_cents(total_cost)

    def create(self, portfolio):
        portfolio.transactions.append(self)
        return self
