#!/usr/bin/python3

from services.fetch_data import fetchStockData
from utils.currency.conversion import to_cents

class DataProcessor:

    __data = None

    
    def fetchData(self):
        self.__data = fetchStockData()


    def stocks_metrics(self):
        if not self.__data:
            self.fetchData()

        data = []

        for dt in self.__data.get("data"):
            stock_data = {}
            stock_data["ticker"] = dt.get("a")
            stock_data["prev"] = dt.get("b")
            stock_data["current"] = dt.get("c")
            stock_data["change"] = dt.get("d")
            stock_data["%change"] = dt.get("e")
            stock_data["high"] = dt.get("f")
            stock_data["low"] = dt.get("g")
            stock_data["volume"] = dt.get("h")
            stock_data["average"] = dt.get("j")

            data.append(stock_data)
        return data 

    def sorted_data_gains(self):
        """ returns stock data list sorted in ascending order according to percentage price gain """

        dataset = self.stocks_metrics()

        for data in dataset:
            if data["change"] != "-":
                data["change"] = (to_cents(data["current"]) - to_cents(data["prev"])) / 100
            else:
                data["change"] = 0
                data["prev"] = 0
        
        
        sorted_data = sorted(dataset, key=lambda obj : (obj.get("change") / float(obj.get("prev"))) if obj.get("prev") != 0 else 0 )
        
        
        return sorted_data

    def top_gainers(self, number=5):
        """ returns top 5 gainers by default if Number not provided """
        data = self.sorted_data_gains()

        if number > len(data):
            msg = f"Number provided {number} is larger than dataset size."
            raise IndexError(msg)
        if number <= 0:
            msg = f"Argument cannot be 0 or Negative"
            raise ValueError(msg)

        segment = number * -1
        segment_data = data[segment:]
        segment_data.reverse()

        return segment_data
    
    def top_losers(self, number = 5):
        """ returns top 5 losers by default if Number not provided """
        data = self.sorted_data_gains()

        if number > len(data):
            msg = f"Number provided {number} is larger than dataset size."
            raise IndexError(msg)
        if number <= 0:
            msg = f"Argument cannot be 0 or Negative"
            raise ValueError(msg)

        return data[:number]

    def market_metrics(self):
        if not self.__data:
            self.fetchData()

        data = {}

        data["volume"] = self.__data.get("v")
        data["deals"] = self.__data.get("d")
        data["turnover"] = self.__data.get("t")
        data["status"] = self.__data.get("s")

        return data
