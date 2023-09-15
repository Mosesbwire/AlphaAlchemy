#!/usr/bin/python3

"""
    Module: stock_service
    contains the business logic associated with the Stock class
"""

from datetime import datetime, timezone
import json
import models
from models.stock import Stock
import requests
from validator_collection import validators, checkers, errors


class StockService:
    """
        class contains all logic required for the correct functioning of the Stock model
    """
    
    def create(self, ticker, name, sector):
        """ interface used to create a Stock instance
            
            Args:
                name: this is the company name as listed on the stock exchange
                ticker: ticker symbol of the company on the exchange
                sector: sector of the economy the company operates in

            Returns:
                dict
                    stock: instance of stock
                    error: list that holds error that occur
        """
        error = []
        try:
            name = validators.string(name.strip(), allow_empty = False)

        except errors.EmptyValueError as e:
            error.append("Name cannot be empty")


        try:
            ticker = validators.string(ticker.strip(), allow_empty = False)

        except errors.EmptyValueError as e:
            error.append("Ticker symbol cannot be empty")
        

        try:
            sector = validators.string(sector.strip(), allow_empty = False)

        except errors.EmptyValueError as e:
            error.append("Sector name cannot be empty")

        if len(error) != 0:
            return {"stock": None, "error": error}
        
        stock = Stock(name, ticker, sector)

        if not stock:
            return {"stock": None, "error": ["Failed to create stock"]}
        
        try:
            models.storage.new(stock)
        except Exception as e:
            print(f"Error occured: {e}")
            stock = None
            error = [e]
        else:
            models.storage.save()

        return {"stock": stock, "error": error}

    def get_stocks(self):
        """ returns a list of stocks """

        stocks = []

        try:
            data = models.storage.all("Stock")

            for stock in data:
                stocks.append(stock.to_dict())
        except Exception as e:
            print(f"Error occured: {e}")
            stocks = []

        return stocks
    
    def get_stock_by_id(self, id):
        """ returns stock with associated id """
    
        stock = None

        try:
            stock = models.storage.get("Stock", id)
        except Exception as e:
            print(f"Error occured: {e}")

        return stock

    def get_stock_by_ticker(self, ticker):
        """ returns first instance that matches with the given name or None """

        stock = None
        try:
            stock = Stock.get_stock_by_ticker(ticker)
        except Exception as e:
            print(f"Error occured: {e}")

        return stock


    def update_stock(self, stock_id, **kwargs):
        """ updates stock attributes """

        error = []
        status_values = ["active", "delisted", "suspended"]
        ticker = kwargs.get("ticker", None)
        name = kwargs.get("name", None)
        sector = kwargs.get("sector", None)
        status = kwargs.get("status", None)

        stock = self.get_stock_by_id(stock_id)

        if stock is None:
            return {"stock": None, "error": ["Stock Not Found"]}

        if name is not None:
            try:
                name = validators.string(name.strip(), allow_empty = False)
                stock.name = name

            except errors.EmptyValueError as e:
                error.append("Name cannot be empty")

        if ticker is not None:

            try:
                ticker = validators.string(ticker.strip(), allow_empty = False)
                stock.ticker = ticker

            except errors.EmptyValueError as e:
                error.append("Ticker symbol cannot be empty")
        
        if sector is not None:
            try:
                sector = validators.string(sector.strip(), allow_empty = False)
                stock.sector = sector
            except errors.EmptyValueError as e:
                error.append("Sector name cannot be empty")

        if status is not None:
            if status.lower() not in status_values:
                error.append("invalid status.\nValid status are active, suspended, delisted.")
            else:
                try:
                    status = validators.string(status.strip(), allow_empty = False)
                    stock.status = status
                except errors.EmptyValueError as e:
                    error.append("Status cannot be empty")

        if len(error) != 0:
            models.storage.roll_back()
            return {"stock": None, "error": error}
       
        stock.updated_at = datetime.now(timezone.utc)

        try:
            models.storage.save()
        except Exception as e:
            stock = None
            error = [e]
        return {"stock": stock, "error": error}



        
