#!/usr/bin/python3

from api.v1.views import app_views
from controllers.stocks import StockController
from flask import abort, jsonify, make_response
from services.data_processor import DataProcessor


processor = DataProcessor()


@app_views.route("/market-data", methods=["GET"])
def get_market_data():

    return make_response(jsonify(processor.aggregated_market_perfomance_data()))


@app_views.route("/stocks", methods=["GET"])
def get_stock_data():
    resp = StockController.all_stocks()

    return resp
