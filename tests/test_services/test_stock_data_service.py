#!/usr/bin/python3

"""
    Module: stock_data_service

    Contains tests fro the StockDataService

"""
from services.stock_data_service import StockDataService
from services.stock_service import StockService
import unittest


class TestStockDataService(unittest.TestCase):
    """ Tests for the StockDataService """

    def setUp(self):
        """ init service instance """

        service = StockDataService()
        stockService = StockService()


    def test_create_function_return_dict(self):
        """ test the create function """




