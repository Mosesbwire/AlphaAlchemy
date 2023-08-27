#!/usr/bin/python3
"""
    Module: stock_data_service
    Contains StockDataService class
"""

import models
from models.stock_data import StockData
from services.stock_service import StockService
from utils.currency.conversion import to_cents, to_unit_currency

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

        
        for key, value in kwargs.items():
            if value == " " or value == "_":
                kwargs[key] = 0

            if key in self.monetary_values:

                kwargs[key] = to_cents(kwargs[key])

        del kwargs["ticker"]
        

        stockData = StockData(**kwargs)

        stock.data.append(stockData)

        models.storage.save()

        return {"data": stockData, "error": None}

    
