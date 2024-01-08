#!/usr/bin/python3

import requests
from utils.currency.conversion import to_cents

DAILY_PRICE_API_URL = "https://tickers.mystocks.co.ke/ticker/J$ON:RMW?app=FIB"

STOCK_API_URL = "https://live.mystocks.co.ke/ajax/stocksectors/"


class FetchData:

    market_data = {}

    @staticmethod
    def format_volume_string(string):
        new_str: int = 0
        if "," in string:
            new_str = int(string.replace(",", ""))
        if "M" in string:
            temp_val = float(string.replace("M", ""))
            new_str = int(temp_val * 1000000)
        return new_str

    @classmethod
    def get_stock_action(cls):
        price_data = requests.get(DAILY_PRICE_API_URL).json()
        cls.market_data = price_data
        action = price_data["data"]
        for at in action:
            price = 0
            try:
                price = float(at.pop("c"))
            except:
                price = 0
            vol = at.pop("h")
            vol = FetchData.format_volume_string(vol)
            at["ticker"] = at.pop("a")
            at["volume"] = vol
            at["price"] = price
        return action

    @staticmethod
    def get_stocks():
        raw_stock_data = requests.get(STOCK_API_URL).json()
        stocks = []
        unique_ticker = set()
        for sector, companies in raw_stock_data.items():
            for ticker, company in companies.items():
                if ticker not in unique_ticker:
                    stocks.append(
                        {"ticker": ticker, "sector": sector, "name": company})
                unique_ticker.add(ticker)
        return stocks

    @classmethod
    def market_activity(cls):
        market_data = {}
        if cls.market_data:
            market_data["volume"] = cls.market_data["v"]
            market_data["deals"] = cls.market_data["d"]
            market_data["turnover"] = cls.market_data["t"]
            market_data["status"] = cls.market_data["s"]
        return market_data
