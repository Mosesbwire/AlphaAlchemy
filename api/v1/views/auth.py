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

    return make_response(jsonify({"token": token.decode("utf-8")}), 200)


def is_authenticated(func):
    
    @wraps(func)
    def inner_func(*args, **kwargs):
        auth_token = request.headers.get("x-auth-token", None)

        if not auth_token:
            raise AuthenticationFailed("Missing header x-auth-token")
        user_id = None
        try:
            data = jwt.decode(auth_token, os.getenv("SECRET_KEY"), algorithm=["HS256"])
            user = data.get("user")
            user_id = user.get("id")
            user = service.get_user_by_id(user_id)
            kwargs["user"] = user
        except:
            raise AuthenticationFailed("Invalid/Expired Token. Login")

        return func(*args,**kwargs)
    return inner_func


@app_views.route("/auth/", methods = ["GET"])
@is_authenticated
def load_user(user=None):
    
    
    if user is None:
        abort(404)

    return make_response(jsonify({"user": user.to_dict()}), 200)

