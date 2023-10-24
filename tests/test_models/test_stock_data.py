#!/usr/bin/python3

"""

    Module: test_stock_data
    Contains unittest for the stock_data class
"""

from models.stock_data import StockData
import unittest


class TestStockData(unittest.TestCase):

    """ test class for the stock data class """

    def test_value_error_raised_on_price_negative(self):
        """test that price cannot be set if it is less than zero"""
        self.assertRaises(ValueError, StockData, -5, 1000)

    def test_value_error_raised_on_volume_negative(self):
        """test that volume cannot be set if it is less than zero"""

        self.assertRaises(ValueError, StockData, 5, -1000)
