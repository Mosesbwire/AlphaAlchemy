#!/usr/bin/python3

"""

    Module: test_portfolio
    Contains unittest for the portfolio class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.portfolio import Portfolio
import unittest


attributes = ["name", "capital", "status"]

class TestPortfolio(unittest.TestCase):

    """ test class for the stock data class """
    def setUp(self):
        """ instantiate data point to be used in the tests """

        self.portfolio = Portfolio("cost-averaging", 70000)
        data = {
            "name": "defensive",
            "capital": 50000
        }

        self.superPortfolio = Portfolio(**data)

    def test_is_subclass(self):
        """ test that stock inherits from the BaseModel """

        self.assertIsInstance(self.portfolio, BaseModel)
        self.assertIsInstance(self.superPortfolio, BaseModel)

        self.assertTrue(hasattr(self.portfolio, "id"))
        self.assertTrue(hasattr(self.portfolio, "created_at"))
        self.assertTrue(hasattr(self.portfolio, "updated_at"))
        self.assertTrue(hasattr(self.superPortfolio, "id"))
        self.assertTrue(hasattr(self.superPortfolio, "created_at"))
        self.assertTrue(hasattr(self.superPortfolio, "updated_at"))

    def test_portfolio_attributes_present(self):
        """ test  that all data attributes are present """
        for attr in attributes:
            with self.subTest(attr=attr):
               self.assertTrue(hasattr(self.portfolio, attr))

    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.portfolio.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertIn(attr, instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[Portfolio] ({self.portfolio.id}) {self.portfolio.__dict__}"
        actual = str(self.portfolio)
        self.assertEqual(expected, actual)

