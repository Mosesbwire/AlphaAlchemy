#!/usr/bin/python3

import requests
from utils.currency.conversion import to_cents

DAILY_PRICE_API_URL = "https://tickers.mystocks.co.ke/ticker/J$ON:RMW?app=FIB"

STOCK_API_URL = "https://live.mystocks.co.ke/ajax/stocksectors/"


class FetchData:

    @staticmethod
    def format_volume_string(string):
        new_str: int = 0
        if "," in string:
            new_str = int(string.replace(",", ""))
        if "M" in string:
            temp_val = float(string.replace("M", ""))
            new_str = int(temp_val * 1000000)
        return new_str

    @staticmethod
    def get_stock_action():
        price_data = requests.get(DAILY_PRICE_API_URL).json()
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
        for sector, companies in raw_stock_data.items():
            for ticker, company in companies.items():
                stocks.append(
                    {"ticker": ticker, "sector": sector, "name": company})

        return stocks
