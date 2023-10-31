#!/usr/bin/python3

"""

    Module: test_portfolio_stock
    Contains unittest for the PortfolioStock class
"""

from models.base_model import BaseModel
from models.portfolio_stock import PortfolioStock
import unittest


attributes = ["quantity"]


class TestPortfolioStock(unittest.TestCase):

    """ test class for the PortfolioStock class """
