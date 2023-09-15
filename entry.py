#!/usr/bin/python3

import requests
import models
from services.data_processor import DataProcessor

from services.stock_service import StockService
from services.user_service import UserService

API_URL = "https://live.mystocks.co.ke/ajax/stocksectors/"
if __name__ == "__main__":
     
    service = StockService()

    data = requests.get(API_URL)

    data = data.json()

    for sector, companies in data.items():
        for ticker, company in companies.items():
            str = f"{sector}| {company} | {ticker}"
            service.create(company, ticker, sector)
            print(str)

    models.storage.save()
    
    """
    s = UserService()

    s.create("John","Doe", "johndoe@gmail.com", "P@ssword1", "P@ssword1")

    models.storage.save()
    """
    
