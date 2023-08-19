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
    def setUp(self):
        """ instantiate a individual stock to be used in the tests """

        self.stock = Stock("SCOM","Safaricom", "Communication and technology")
        data = {
            "ticker": "KCB",
            "name": "Kenya Commercial Bank",
            "sector": "Banking",
        }

        self.superStock = Stock(**data)

    def test_is_subclass(self):
        """ test that stock inherits from the BaseModel """

        self.assertIsInstance(self.stock, BaseModel)
        self.assertIsInstance(self.superStock, BaseModel)

        self.assertTrue(hasattr(self.stock, "id"))
        self.assertTrue(hasattr(self.stock, "created_at"))
        self.assertTrue(hasattr(self.stock, "updated_at"))
        self.assertTrue(hasattr(self.superStock, "id"))
        self.assertTrue(hasattr(self.superStock, "created_at"))
        self.assertTrue(hasattr(self.superStock, "updated_at"))

    def test_name(self):
        """ test that stock has attribute name """
        self.assertTrue(hasattr(self.stock, "name"))
        self.assertTrue(hasattr(self.superStock, "name"))

    def test_ticker_name(self):
        """ test stock has attribute ticker """

        self.assertTrue(hasattr(self.stock, "ticker"))
        self.assertTrue(hasattr(self.superStock, "ticker"))

    def test_sector_name(self):
        """ test user has attribute sector """
        self.assertTrue(hasattr(self.stock, "ticker"))
        self.assertTrue(hasattr(self.superStock, "ticker"))
    
    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.stock.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("ticker", instance_dict)
        self.assertIn("name", instance_dict)
        self.assertIn("sector", instance_dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[Stock] ({self.stock.id}) {self.stock.__dict__}"
        actual = str(self.stock)

        self.assertEqual(expected, actual)

