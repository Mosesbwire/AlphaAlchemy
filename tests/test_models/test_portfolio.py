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

    @patch("models.portfolio.models")
    def test_valuation_is_calculated_correctly(self, mock_db):
        """test that valuation is calculated using recent data"""

        mock_db.storage.execute.return_value = [
            {"ticker": "SCOM", "quantity": 200},
            {"ticker": "EQTY", "quantity": 200}
        ]

        stock_data = [
            {"ticker": "SCOM", "price": 13.00},
            {"ticker": "EQTY", "price": 37.95}
        ]
        portfolio = Portfolio()

        expected_valuation = 10190.0
        actual_valuation = portfolio.portfolio_stocks_valuation(stock_data)
        mock_db.stop()
        self.assertEqual(expected_valuation, actual_valuation)
        mock_db.storage.execute.assert_called_once()
