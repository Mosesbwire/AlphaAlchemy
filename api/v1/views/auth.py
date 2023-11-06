#!/usr/bin/python3

from api.v1.views import app_views
from controllers.users import UserController
from flask import jsonify, make_response, request
from services.auth import Auth


@app_views.route("/", methods=["GET"])
def api_status():
    return make_response(jsonify({"status": "OK"}), 200)


@app_views.route("/auth/login", methods=["POST"])
def login():
    resp = UserController.login(request)
    return resp


@app_views.route("/auth/", methods=["GET"])
@Auth.is_authenticated
def load_user():
    resp = UserController.get_user_by_id(request)
    return resp
