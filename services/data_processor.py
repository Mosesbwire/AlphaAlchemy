#!/usr/bin/python3

from services.fetch_data import FetchData
from utils.currency.conversion import to_cents


class DataProcessor:

    __data = None

    def __init__(self):
        self.fetchData()

    def fetchData(self):
        self.__data = FetchData.get_stock_action()

    def stocks_metrics(self):
        if not self.__data:
            self.fetchData()

        data = []
        if self.__data:
            for dt in self.__data:
                stock_data = {}
                stock_data["ticker"] = dt.get("ticker")
                stock_data["prev"] = dt.get("b")
                stock_data["current"] = dt.get("price")
                stock_data["change"] = dt.get("d")
                stock_data["%change"] = dt.get("e")
                stock_data["high"] = dt.get("f")
                stock_data["low"] = dt.get("g")
                stock_data["volume"] = dt.get("volume")
                stock_data["average"] = dt.get("j")

                data.append(stock_data)

        return data

    def sorted_data_gains(self):
        """ returns stock data list sorted in ascending order according to percentage price gain """

        dataset = self.stocks_metrics()

        for data in dataset:

            if data["change"] != "-":
                data["change"] = (to_cents(data["current"]) -
                                  to_cents(data["prev"])) / 100
            else:
                data["change"] = 0
                data["prev"] = 0

        sorted_data = sorted(dataset, key=lambda obj: (
            obj.get("change") / float(obj.get("prev"))) if obj.get("prev") != 0 else 0)

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

    def top_losers(self, number=5):
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

        return FetchData.market_activity()

    def sorted_by_volume(self):
        """ returns stock market data sorted by volume in ascending order"""
        dataset = self.stocks_metrics()

        sorted_data = sorted(dataset, key=lambda obj: int(obj.get("volume")))

        return sorted_data

    def aggregated_market_perfomance_data(self):
        """ returns aggregated data for the current perfomance of the market """
        data = {}
        losers = self.top_losers()
        gainers = self.top_gainers()
        stocks = self.stocks_metrics()
        market_metrics = self.market_metrics()
        volume = self.sorted_by_volume()

        data["losers"] = losers
        data["gainers"] = gainers
        data["stocks"] = stocks
        data["market_metrics"] = market_metrics

        movers = volume[-5:]
        movers.reverse()
        data["movers"] = movers

        return data

    def current_stock_price(self, ticker):
        """ returns the latest price of a stock """
        latest_market_data = self.stocks_metrics()
        for data in latest_market_data:
            if data["ticker"] == ticker:
                return data["current"]
