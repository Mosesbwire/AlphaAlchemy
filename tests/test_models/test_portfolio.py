#!/usr/bin/python3

"""

    Module: test_portfolio
    Contains unittest for the portfolio class
"""
from dotmap import DotMap
from models.portfolio import Portfolio
import unittest
from unittest.mock import Mock, patch


class TestPortfolio(unittest.TestCase):

    """ test class for the stock data class """

    @patch("models.portfolio.models")
    def test_valuation_is_calculated_correctly(self, mock_db):
        """test that valuation is calculated using recent data"""

        mock_db.storage.execute.return_value = [
            DotMap(ticker="SCOM", quantity=200),
            DotMap({"ticker": "EQTY", "quantity": 200})
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

    def test_lot_size_is_multiple_of_100(self):
        portfolio = Portfolio()
        self.assertTrue(portfolio.valid_lot_size(200))

    def test_lot_size_false_not_multiple_100(self):
        portfolio = Portfolio()
        self.assertFalse(portfolio.valid_lot_size(101))

    @patch("models.portfolio.Transaction")
    def test_transaction_is_created(self, mock_transaction):
        """test that a transaction is created when a stock is bought/sold"""

        portfolio = Portfolio()
        mock_stock = Mock()
        mock_stock.stock_ticker.return_value = "SCOM"
        mock_stock.id.return_value = "scom_id"
        instance = mock_transaction.return_value

        return_value = "TRANSACTION"
        instance.create.return_value = return_value
        transaction = portfolio.create_order_transaction(
            mock_stock, 12.40, 100, "buy")

        mock_transaction.stop()

        self.assertEqual(transaction, return_value)
        instance.create.assert_called_once()
        instance.create.assert_called_with(portfolio)

    def test_none_is_returned_on_incorrect_values(self):
        """test a transaction is not created if passed incorrect values"""
        portfolio = Portfolio()
        mock_stock = Mock()
        mock_stock.stock_ticker.return_value = "SCOM"
        mock_stock.id.return_value = "scom_id"

        transaction = portfolio.create_order_transaction(
            mock_stock, 0, 0, "buy")

        self.assertIsNone(transaction)

    @patch("models.portfolio.PortfolioStock")
    def test_portfolio_stock_is_created(self, mock_portfolio_stock):
        """test portfoliostock is created when stock is bought"""
        portfolio = Portfolio()
        mock_stock = Mock()
        mock_stock.stock_ticker.return_value = "SCOM"
        mock_stock.id.return_value = "scom_id"
        instance = mock_portfolio_stock.return_value
        ps = "PORTFOLIO_STOCK"
        instance.create.return_value = ps
        mock_portfolio_stock.stop()

        with self.subTest("Test adding existing stock, quantity is increased"):
            portfolio_st_mock = Mock()
            portfolio_st_mock.stock_quantity = 100
            portfolio_stock = portfolio.add_stock(
                mock_stock, 100, portfolio_st_mock)
            if portfolio_stock:
                actual_qty = portfolio_stock.stock_quantity
                expected_qty = 200
                self.assertEqual(actual_qty, expected_qty)
        with self.subTest("Test new instance is created when adding new stock"):
            portfolio_stock = portfolio.add_stock(mock_stock, 100)
            self.assertEqual(portfolio_stock, ps)
            instance.create.assert_called_once()

    def test_buy_action_is_successful(self):
        """test that a buy action is successful"""

        portfolio = Portfolio()
        mock_stock = Mock()
        mock_stock.stock_ticker.return_value = "SCOM"
        mock_stock.id.return_value = "scom_id"

        instance = portfolio.buy_stock(12.05, 200, mock_stock)

        self.assertIsInstance(instance, Portfolio)
        self.assertEqual(instance, portfolio)

    def test_buy_action_not_successful(self):
        """test value error is raised on incorrect quantity"""
        portfolio = Portfolio()
        mock_stock = Mock()
        mock_stock.stock_ticker.return_value = "SCOM"
        mock_stock.id.return_value = "scom_id"

        self.assertRaises(ValueError, portfolio.buy_stock,
                          12.05, 199, mock_stock)
