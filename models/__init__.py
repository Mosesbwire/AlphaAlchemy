#!/usr/bin/python3

"""
    initialize the models package
"""

from models.engine.storage import Storage
from models.stock import Stock
from services.fetch_data import FetchData
import os

DB_NAME = os.getenv("DATABASE")
DB_USERNAME = os.getenv("USERNAME")
DB_PASSWORD = os.getenv("PASSWORD")
DB_HOST = os.getenv("HOST")
DB_PORT = os.getenv("PORT")


# DB_URL = f"mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
DB_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

storage = Storage(DB_URL)
storage.reload()

dbStockData = Stock.get_stocks()
print(dbStockData)
if os.getenv("ENV") == "PRODUCTION" and not dbStockData:
    stocks = FetchData.get_stocks()

    for stock in stocks:

        try:
            st = Stock(stock["ticker"], stock["name"], stock["sector"])
            st.save()
        except ValueError as e:
            print("Error occured")
        except Exception as e:
            print(f'MYSQL ERROR: {e}')
