#!/usr/bin/env python3

# portfolio.py

from flask import make_response, jsonify
from models.portfolio import Portfolio
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
    def get_portfolio(req):
        pass
