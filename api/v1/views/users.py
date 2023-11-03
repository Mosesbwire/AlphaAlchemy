#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest
from api.v1.views.auth import is_authenticated

from flask import abort, jsonify, make_response, request, Response
import jwt
import os
from services.user_service import UserService
from services.stock_service import StockService
from services.auth import Auth
from controllers.users import UserController

service = UserService()
stockService = StockService()


@app_views.route("/users", methods=["POST"])
def create_user():
    res = UserController.create(request)
    return res


@app_views.route("/users", methods=["GET"])
@Auth.is_authenticated
def get_users():
    users_list = []
    users = service.get_users()

    for user in users:
        users_list.append(user.to_dict())

    return jsonify(users_list)


@app_views.route("/users/<user_id>", methods=["GET"])
@Auth.is_authenticated
def get_user(user_id):

    user = service.get_user_by_id(user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=["PUT"])
@Auth.is_authenticated
def update_user(user_id):
    data = request.get_json()
    if not data:
        raise BadRequest("Request body is empty")


@app_views.route("/users/<user_id>", methods=["DELETE"])
@Auth.is_authenticated
def delete_user(user_id):
    resp = service.delete_user(user_id)

    if resp is None:
        abort(404)
    return make_response(jsonify({"message": "User account successfully deleted."}))
