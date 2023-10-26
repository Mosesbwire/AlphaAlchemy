#!/usr/bin/python3

"""

    Module: test_portfolio
    Contains unittest for the portfolio class
"""

from models.portfolio import Portfolio
import unittest
from unittest.mock import Mock, patch


class TestPortfolio(unittest.TestCase):

    """ test class for the stock data class """

    def test_create_function_appends_portfolio_to_user(self):
        portfolio = Portfolio()
        user = Mock()

    def test_valuation_is_calculated_correctly(self):
        """test that valuation is calculated using recent data"""
