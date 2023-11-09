#!/usr/bin/python3

from api.v1.views import app_views
from flask import request
from services.auth import Auth
from controllers.users import UserController


@app_views.route("/users", methods=["POST"])  # type: ignore
def create_user():
    res = UserController.create(request)
    return res


@app_views.route("/users/portfolio", methods=["GET"])
@Auth.is_authenticated
def get_portfolio():

    res = UserController.get_portfolio(Auth.logged_user(request))
    return res


@app_views.route("/users/portfolio/status", methods=["GET"])
@Auth.is_authenticated
def has_portfolio():
    res = UserController.user_has_portfolio(Auth.logged_user(request))
    return res
