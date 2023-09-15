#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.views.auth import is_authenticated
from flask import abort, jsonify, make_response, request
from services.data_processor import DataProcessor
from services.stock_service import StockService

processor = DataProcessor()
stockService = StockService()

@app_views.route("/market-data", methods = ["GET"])
@is_authenticated
def get_market_data():
    
    return make_response(jsonify(processor.aggregated_market_perfomance_data()))

@app_views.route("/stocks", methods = ["GET"])
@is_authenticated

def get_stock_data():
    data = stockService.get_stocks()

    if len(data) == 0:
        abort(404)

    return make_response(jsonify(data))
