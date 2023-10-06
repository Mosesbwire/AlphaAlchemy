#!/usr/bin/python3

from api.v1.views import app_views
from api.v1.error import BadRequest, AuthenticationFailed
import bcrypt
from flask import abort, jsonify, make_response, request
from functools import wraps
import jwt
from services.user_service import UserService
import os

service = UserService()

@app_views.route("/", methods=["GET"])
def api_status():
    return make_response(jsonify({"status": "OK"}), 200)


@app_views.route("/auth/login", methods =["POST"])
def login():
    data = request.get_json()

    if not data:
        raise BadRequest("Body can not be empty")

    if "email" not in data:
        raise BadRequest("Email is missing")
    if "password" not in data:
        raise BadRequest("Password is missing")
    
    user = service.get_user_by_email(data.get("email"))

    if user is None:
        abort(404)
    
    input_password = data.get("password").encode("utf-8")

    if not bcrypt.checkpw(input_password, user.password.encode("utf-8")):
        raise BadRequest("Invalid Email or Password")
    
    token = jwt.encode({
            "user": {"id": user.id}
        }, os.getenv("SECRET_KEY"), algorithm="HS256")

    return make_response(jsonify({"token": token}), 200)


def is_authenticated(func):
    
    @wraps(func)
    def inner_func(*args, **kwargs):
        auth_token = request.headers.get("x-auth-token", None)

        if not auth_token:
            raise AuthenticationFailed("Missing header x-auth-token")
        user_id = None
        try:
            data = jwt.decode(auth_token, os.getenv("SECRET_KEY"), algorithms="HS256")
            user = data.get("user")
            user_id = user.get("id")
            if "user_id" in func.__code__.co_varnames:
                kwargs["user_id"] = user_id
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Expired Token. Login")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid Token")
        except Exception as e:
            print(e)
            make_response(jsonify({"error": "error occured"}))
        return func(*args, **kwargs)
    return inner_func


@app_views.route("/auth/", methods = ["GET"])
@is_authenticated
def load_user(user_id):
    
    user = service.get_user_by_id(user_id)
    
    if user is None:
        abort(404)
    balance = user.balance / 100
    user = user.to_dict()
    user["balance"] = balance
    return make_response(jsonify({"user": user}), 200)

