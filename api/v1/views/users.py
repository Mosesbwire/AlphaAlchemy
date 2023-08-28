#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest
from flask import abort, jsonify, make_response, request
from services.user_service import UserService


service = UserService()


@app_views.route("/users", methods = ["POST"])
def create_user():
    data = request.get_json()
    
    if not data:
        raise BadRequest("Request Body is empty")

    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    email = data.get("email", "")
    password = data.get("password", "")
    confirm_password = data.get("confirm_password", "")

    user_data = service.create(first_name, last_name, email, password, confirm_password)

    if user_data.get("error"):
        raise BadRequest(user_data.get("error"))

    return make_response(jsonify(user_data.get("user").to_dict()), 201)


@app_views.route("/users", methods = ["GET"])

def get_users():
    users_list = []
    users = service.get_users()

    for user in users:
        users_list.append(user.to_dict())
    
    return jsonify(users_list)

@app_views.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):

    user = service.get_user_by_id(user_id)

    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        raise BadRequest("Request body is empty")


@app_views.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    resp = service.delete_user(user_id)

    if resp is None:
        abort(404)
    return make_response(jsonify({"message": "User account successfully deleted."}))
