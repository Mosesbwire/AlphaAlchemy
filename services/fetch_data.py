#!/usr/bin/python3

import requests

API_URL = "https://tickers.mystocks.co.ke/ticker/J$ON:RMW?app=FIB"


def fetchStockData():
    data = requests.get(API_URL)
    return data.json()
