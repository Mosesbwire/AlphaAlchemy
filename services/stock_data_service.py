#!/usr/bin/python3
"""
    Module: stock_data_service
    Contains StockDataService class
"""

import models
from models.stock_data import StockData
import requests
from services.data_processor import DataProcessor
from services.stock_service import StockService
from utils.currency.conversion import to_cents, to_unit_currency


dataProcessor = DataProcessor()

class StockDataService:
    """ Class responsible for fetching a stocks data
        responsible for inserting daily stock data to db
    """
    monetary_values = ["prev", "current", "high", "low", "average"]
    
    def create(self, **kwargs):
        """ Creates an instance of StockData """

        error = []
        
        ticker = kwargs.get("ticker", None)
    
        if ticker is None:
            msg = "ticker symbol can not be empty"
            raise ValueError(msg)

        stock = StockService().get_stock_by_ticker(ticker)

        if stock is None:
            return {"data": None, "error": ["Stock not found"]}

        data_dict = {}

        for key, value in kwargs.items():
            data_dict[key] = value
            if value == " " or value == "_" or value == "-":
                data_dict[key] = 0

            if key in self.monetary_values:

                data_dict[key] = to_cents(data_dict[key])

        del data_dict["ticker"]
        

        stockData = StockData(**data_dict)

        stock.data.append(stockData)

        models.storage.save()

        return {"data": stockData, "error": None}
    
    def add_daily_stock_data(self):
        stock_data = dataProcessor.stocks_metrics()

        for stock in stock_data:
            self.create(**stock)

