#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest
from api.v1.views.auth import is_authenticated
from flask import abort, jsonify, make_response, request
from services.portfolio_service import PortfolioService
from services.user_service import UserService

service = PortfolioService()
userService = UserService()

@app_views.route("/portfolios", methods = ["POST"])
@is_authenticated
def create_portfolio(user_id):
    
    data = request.get_json()

    if not data:
        raise BadRequest("Request body is Empty")

    name = data.get("name")
    
    user = userService.get_user_by_id(user_id)
    
    if user is None:
        abort(404)

    portfolio_data = service.create(user.id, name)

    if portfolio_data.get("error"):
        raise BadRequest(portfolio_data.get("error"))

    portfolio = portfolio_data.get("portfolio")
    portfolio = portfolio.to_dict()
    del portfolio["user"]
    return make_response(jsonify(portfolio))

@app_views.route("/portfolios/<id>", methods = ["GET"])
@is_authenticated
def get_portfolio_by_id(id):
    portfolio = service.get_portfolio_details(id)
    if portfolio is None:
        abort(404)

    return make_response(jsonify(portfolio))

@app_views.route("/portfolios", methods = ["GET"])
@is_authenticated
def get_user_portfolios(user_id):
    portfolios = service.get_user_portfolios(user_id)

    return make_response(jsonify(portfolios))

@app_views.route("/portfolios/<portfolio_id>/buy", methods = ["POST"])
@is_authenticated

def buy_stocks(portfolio_id, user_id):
    data = request.get_json()

    if not data:
        raise BadRequest("Request Body is empty")
    stock_id = data.get("security", None)
    quantity = data.get("quantity", None)
    bid_price = data.get("price", None)

    transaction = service.buy_action(user_id, portfolio_id, stock_id, float(quantity), float(bid_price))
    error = transaction.get("error")

    if error:
        raise BadRequest(error)
    
    data = transaction.get("transaction")
    data = data.to_dict()
    del data["portfolio"]
    return make_response(jsonify(data))

@app_views.route("/portfolios/<portfolio_id>/sell", methods = ["POST"])
@is_authenticated

def sell_stock(portfolio_id, user_id):
    data = request.get_json()

    if not data:
        raise BadRequest("Request body is empty")

    stock_id = data.get("security", None)
    quantity = data.get("quantity", None)
    ask_price = data.get("price", None)

    transaction = service.sell_action(user_id, portfolio_id, stock_id, float(quantity), float(ask_price))

    error = transaction.get("error")

    if error:
        raise BadRequest(error)

    data = transaction.get("transaction")
    data = data.to_dict()
    del data["portfolio"]

    return make_response(jsonify(data))

@app_views.route("/portfolio/<portfolio_id>/transactions", methods = ["GET"])
@is_authenticated

def get_portfolio_transactions(portfolio_id):
    
    transactions = []
    transaction_objects = service.get_portfolio_transactions(portfolio_id)

    for transaction in transaction_objects:
        transactions.append(transaction.to_dict())

    return make_response(jsonify(transactions))
