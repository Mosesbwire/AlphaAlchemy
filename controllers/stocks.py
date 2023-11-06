#!/usr/bin/env python3

# stocks.py

from flask import make_response, jsonify
from models.stock import Stock


class StockController:

    @staticmethod
    def all_stocks():
        stocks = Stock.get_stocks()
        if not stocks:
            return make_response(jsonify({"error": {
                "message": "Failed to fetch stocks. Try again"
            }}), 500)

        def to_dict(stock):
            return stock.to_dict()

        data = map(to_dict, stocks)

        return make_response(jsonify({"stocks": list(data)}), 200)
