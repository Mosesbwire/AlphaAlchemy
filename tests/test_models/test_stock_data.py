#!/usr/bin/python3

"""

    Module: test_stock_data
    Contains unittest for the stock_data class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.stock import Stock
from models.stock_data import StockData
import unittest


attributes = ["prev", "current", "price_change", "percentage_price_change", "high", "low", "volume", "average", "time"]

class TestUser(unittest.TestCase):

    """ test class for the stock data class """
    def setUp(self):
        """ instantiate data point to be used in the tests """

        self.stockData = StockData("10.09","12.00", "2.09", "34.65%", "13.45", "10.09", "45000", "11.05", "time")
        data = {
            "prev": 12.00,
            "current": 9.00,
            "price_change": 3.00,
            "percentage_price_change": 20,
            "high": 15.00,
            "low": 9.00,
            "volume": 6000,
            "average": 10.00,
            "time": "time"
        }

        self.superStockData = StockData(**data)

    def test_is_subclass(self):
        """ test that stock inherits from the BaseModel """

        self.assertIsInstance(self.stockData, BaseModel)
        self.assertIsInstance(self.superStockData, BaseModel)

        self.assertTrue(hasattr(self.stockData, "id"))
        self.assertTrue(hasattr(self.stockData, "created_at"))
        self.assertTrue(hasattr(self.stockData, "updated_at"))
        self.assertTrue(hasattr(self.superStockData, "id"))
        self.assertTrue(hasattr(self.superStockData, "created_at"))
        self.assertTrue(hasattr(self.superStockData, "updated_at"))

    def test_stock_data_attributes_present(self):
        """ test  that all data attributes are present """
        for attr in attributes:
            with self.subTest(attr=attr):
               self.assertTrue(hasattr(self.stockData, attr))

    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.stockData.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertIn(attr, instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[StockData] ({self.stockData.id}) {self.stockData.__dict__}"
        actual = str(self.stockData)
        self.assertEqual(expected, actual)

