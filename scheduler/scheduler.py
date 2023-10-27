#!/usr/bin/python3


import schedule
import time
from models.stock import Stock
from models.stock_data import StockData
from services.fetch_data import FetchData


def get_price_action_job():
    stock_data_action = FetchData.get_stock_action()
    print('Fetching')
    for data in stock_data_action:
        stock = Stock.get_stock_by_ticker(data["ticker"])
        if stock:
            stock_data = StockData(data["price"], data["volume"])
            stock.data.append(stock_data)
            stock_data.save()


schedule.every(10).minutes.do(get_price_action_job)


if __name__ == "__main__":
    while True:

        schedule.run_pending()
        time.sleep(1)
