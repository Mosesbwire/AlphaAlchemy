#!/usr/bin/python3

"""
    Module: test_stock_service
    Contains test for the StockService module
"""
from models.stock import Stock
from services.stock_service import StockService
import unittest


class TestStockService(unittest.TestCase):
    """ Unit tests for the StockService class """

    def setUp(self):
        """ initialize service instance """

        self.service = StockService()

    def test_create_function_return_dict(self):
        """ test that create returns a dict """

        data = self.service.create("safaricom", "SCOM", "Communication")
        
        self.assertIsInstance(data, dict)
        self.assertIn("stock", data)
        self.assertIn("error", data)

    def test_create_returns_stock(self):
        """ test that a stock is created when given valid data """
        
        name = "KCB"
        ticker = "KCB"
        sector = "BANKING"
        data = self.service.create(ticker, name, sector)

        stock = data.get("stock")

        self.assertIsInstance(stock, Stock)
        self.assertEqual(stock.name, name)
        self.assertEqual(stock.ticker, ticker)
        self.assertEqual(stock.sector, sector)
        self.assertEqual(stock.status, "active")
    
    def test_create_returns_error_on_invalid_data(self):
        """ test that validations catch invalid parameter data """

        data = self.service.create("", "", "")
        
        expected_error_msg = ["Name cannot be empty", "Ticker symbol cannot be empty",\
                "Sector name cannot be empty"]

        error = data.get("error")

        for idx, err in enumerate(expected_error_msg):
            with self.subTest(err = err):
                self.assertEqual(error[idx], err)

    def test_get_stocks(self):
        """ returns a list """
        stocks = self.service.get_stocks()

        self.assertIsInstance(stocks, list)

    def test_get_stock_by_id(self):
        """ returns Stock instance from database """

        data = self.service.create("NCBA", "NCBA", "Banking")

        stock = data.get("stock")

        id = stock.id
        
        fetchedStock = self.service.get_stock_by_id(id)

        self.assertIs(stock, fetchedStock)

    def test_get_stock_by_id_returns_none(self):
        """ returns none if stock with id does not exist """

        stock = self.service.get_stock_by_id("qwerty")

        self.assertIsNone(stock)

    def test_update_stock_returns_dict(self):
        """ test return value is a dict """

        data = self.service.update_stock("qwerty", ticker = "sasn")

        self.assertIsInstance(data, dict)
        self.assertIn("stock", data)
        self.assertIn("error", data)

    def test_update_stock(self):
        """ updates stocks attributes """

        data = self.service.create("SASN", "Sasini", "Agriculture")

        stock = data.get("stock")

        id = stock.id
        name = "sasini agric inc"

        updated_ticker = "SSN"

        fetchedData = self.service.update_stock(id, ticker = updated_ticker)

        fetchedStock = fetchedData.get("stock")

        self.assertIs(stock, fetchedStock)
        self.assertEqual(fetchedStock.ticker, updated_ticker)
    
    def test_update_stock_return_error_failed_validations(self):
        """ test that error is returned on failed validations """
        stock = self.service.create("SSN", "SASINI", "AGRIC")

        id = stock.get("stock").id

        data = self.service.update_stock(id, name = " ", ticker = " ", sector = " ")
        
        expected_error_msg = ["Name cannot be empty", "Ticker symbol cannot be empty",\
                "Sector name cannot be empty"]

        error = data.get("error")

        for idx, err in enumerate(expected_error_msg):
            with self.subTest(err = err):
                self.assertEqual(error[idx], err)

    def test_update_stock_status_invalid_value(self):
        """ test that error is returned if status passed is invalid """
        
        stock = self.service.create("SSN", "SASINI", "AGRIC")

        id = stock.get("stock").id

        data = self.service.update_stock(id, status = "state")

        expected_error_msg = "invalid status.\nValid status are active, suspended, delisted."
        
        error = data.get("error")

        self.assertEqual(error[0], expected_error_msg)

