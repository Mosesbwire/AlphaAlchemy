#!/usr/bin/env python3

# users.py

"""Handles client requests and coordinates flow of the application"""
from flask import make_response, jsonify
from models.user import User
from services.auth import Auth, AuthenticationError
from services.fetch_data import FetchData
from sqlalchemy import exc
from utils.validate_data import validate_user_data


class UserController:
    """User controller class"""

    @staticmethod
    def create(req):

        data = req.get_json()
        if not data:
            return make_response(jsonify({"error": {
                "message": "Cannot process empty data fields",
                "errors": []
            }}), 400)

        is_errors = validate_user_data(data)

        if is_errors:
            return make_response(jsonify({"error": {
                "message": "Unprocessable Data",
                "errors": is_errors
            }}), 400)
        fname = data.get("first_name")
        lname = data.get("last_name")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            return make_response(jsonify({"error": {
                "message": "Unprocesable data",
                "error": [{"confirm_password": "password must match confirm password"}]
            }}), 400)
        try:
            user = User(fname, lname, email, password)
            if user:
                user.save()
                bal = user.acc_balance
                user = user.to_dict()
                user["balance"] = bal
                return make_response(jsonify(user), 201)
        except ValueError as err:
            return make_response(jsonify({"error": {
                "message": "Unprocessable entity",
                "error": [err]
            }}), 400)
        except exc.IntegrityError as err:
            return make_response(jsonify({"error": {
                "message": "User with email already exists",
                "error": []
            }}), 400)

    @staticmethod
    def login(req):
        data = req.get_json()

        if not data:
            return make_response(jsonify({
                "error": {
                    "message": "Cannot process empty data",
                    "error": [
                        {"email": "Provide a valid email address"},
                        {"password": "provide your password to login"}
                    ]
                }
            }), 400)
        email = data.get("email")
        password = data.get("password")

        user = User.get_user_by_email(email)

        if not user:
            return make_response(jsonify({
                "error": {
                    "message": "User not found",
                    "error": []
                }
            }), 404)

        try:
            jwt_token = Auth.authenticate(user, password)
            return make_response(jsonify(jwt_token), 200)
        except AuthenticationError as err:
            return make_response(jsonify({"error": {
                "message": err.errors,
                "error": [{"password": err.errors}]
            }}), 400)

    @staticmethod
    def get_portfolio(user):
        if not user:
            return make_response(jsonify({"error": {
                "message": "user not found",
                "error": []
            }}), 404)
        portfolio = user.user_portfolio()

        if not portfolio:
            return make_response(jsonify({"User has no portfolio. Create portfolio"}), 200)
        data = FetchData.get_stock_action()
        full_portfolio = {}
        stocks = portfolio.portfolio_details(data)
        valuation = portfolio.portfolio_stocks_valuation(data)
        full_portfolio["stocks"] = stocks
        full_portfolio["market_valuation"] = valuation
        return make_response(jsonify(full_portfolio), 200)
