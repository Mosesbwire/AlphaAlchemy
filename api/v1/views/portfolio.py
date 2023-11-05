#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest
from controllers.portfolio import PortfolioController
from flask import abort, jsonify, make_response, request
from services.auth import Auth
from services.portfolio_service import PortfolioService
from services.user_service import UserService

service = PortfolioService()
userService = UserService()


@app_views.route("/portfolios", methods=["POST"])
@Auth.is_authenticated
def create_portfolio():
    resp = PortfolioController.create(request)
    return resp


@app_views.route("/portfolios/buy", methods=["POST"])
@Auth.is_authenticated
def buy():
    user = Auth.logged_user(request)
    resp = PortfolioController.buy_stock(user, request)

    return resp


@app_views.route("/portfolios/sell", methods=["POST"])
@Auth.is_authenticated
def sell():
    user = Auth.logged_user(request)
    resp = PortfolioController.sell_stock(user, request)

    return resp
