#!/usr/bin/env python3

# portfolio.py

from controllers.users import UserController
from flask import make_response, jsonify
from models.portfolio import Portfolio
from models.stock import Stock
from models.user import User


class PortfolioController:

    @staticmethod
    def create(req):
        user_id = req.user_id
        user = User.get_user_by_id(user_id)

        if not user:
            return make_response(jsonify({"error": {
                "message": "User not found",
                "error": []
            }}), 404)
        portfolio = Portfolio()

        portfolio = portfolio.create(user)

        if not portfolio:
            return make_response(jsonify({"error": {
                "message": "Failed to create portfolio. Try again",
                "error": []
            }}), 500)
        try:
            portfolio.save()
            portfolio_dict = portfolio.to_dict()
            del portfolio_dict["user"]
            return make_response(jsonify({"portfolio": portfolio_dict, "message": "Portfolio was successfuly created"}), 201)
        except Exception as err:
            print(err)
            return make_response(jsonify({"error": {
                "message": "Error occured during save. Try again",
                "error": []
            }}), 500)

    @staticmethod
    def buy_stock(user, req):
        if not user:
            return make_response(jsonify({"error": {
                "message": "User not found",
                "error": []
            }}), 404)
        portfolio = user.user_portfolio()

        if not portfolio:
            return make_response(jsonify({"message": "User does not have a portfolio. Create portfolio"}), 400)

        data = req.get_json()
        stock_id = data.get("stock_id")
        bid_price = data.get("bid_price")
        quantity = data.get("quantity")

        stock = Stock.get_stock_by_id(stock_id)

        if not stock:
            return make_response(jsonify({"message": "Stock not found. The id provided is incorrect"}), 404)
        try:
            updated_portfolio = portfolio.buy_stock(
                float(bid_price), int(quantity), stock)
            if not updated_portfolio:
                return make_response(jsonify({"error": {"message": "Transaction failed"}}), 400)
            user.decrease_balance(float(bid_price))
            portfolio.update()
            resp = UserController.get_portfolio(user)
            return resp
        except ValueError as err:
            msg = err.args[0]
            return make_response(jsonify({"error": msg}), 400)

    @staticmethod
    def sell_stock(user, req):
        if not user:
            return make_response(jsonify({"error": {
                "message": "User not found",
                "error": []
            }}), 404)
        portfolio = user.user_portfolio()

        if not portfolio:
            return make_response(jsonify({"message": "User does not have a portfolio. Create portfolio"}), 400)

        data = req.get_json()
        stock_id = data.get("stock_id")
        ask_price = data.get("ask_price")
        quantity = data.get("quantity")

        stock = Stock.get_stock_by_id(stock_id)

        if not stock:
            return make_response(jsonify({"message": "Stock not found. The id provided is incorrect"}), 404)
        try:
            updated_portfolio = portfolio.sell_stock(
                float(ask_price), int(quantity), stock)
            if not updated_portfolio:
                return make_response(jsonify({"error": {"message": "Transaction failed"}}), 400)
            user.increase_balance(float(quantity))
            portfolio.update()
            resp = UserController.get_portfolio(user)
            return resp
        except ValueError as err:
            msg = err.args[0]
            return make_response(jsonify({"error": msg}), 400)
