#!/usr/bin/python3

"""
    Module: test_stocks
    Contains unittest for the stock class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.stock import Stock
import unittest


class TestStock(unittest.TestCase):
    """ test class for the stock class """

    def test_invalid_ticker_symbol(self):
        """test that ValueError is raised when invalid ticker symbol"""
        self.assertRaises(ValueError, Stock, "LONGTICKER", "NAME", "AGRIC")

    def test_invalid_status(self):
        """test ValueError is raised when invalid status is passed"""
        self.assertRaises(ValueError, Stock, "EQTY",
                          "EQUITY", "AGRIC", "INVALID")
