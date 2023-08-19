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
    def setUp(self):
        """ instantiate stock to be used in the tests """

        self.stock = PortfolioStock(1000)
        data = {
            "quantity": 5000,
        }

        self.superStock = PortfolioStock(**data)

    def test_is_subclass(self):
        """ test that PortfolioStock inherits from the BaseModel """

        self.assertIsInstance(self.stock, BaseModel)
        self.assertIsInstance(self.superStock, BaseModel)

        self.assertTrue(hasattr(self.stock, "id"))
        self.assertTrue(hasattr(self.stock, "created_at"))
        self.assertTrue(hasattr(self.stock, "updated_at"))
        self.assertTrue(hasattr(self.superStock, "id"))
        self.assertTrue(hasattr(self.superStock, "created_at"))
        self.assertTrue(hasattr(self.superStock, "updated_at"))

    def test_stock_attributes_present(self):
        """ test  that all data attributes are present """
        for attr in attributes:
            with self.subTest(attr=attr):
               self.assertTrue(hasattr(self.stock, attr))

    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.stock.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertIn(attr, instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[PortfolioStock] ({self.stock.id}) {self.stock.__dict__}"
        actual = str(self.stock)
        self.assertEqual(expected, actual)

