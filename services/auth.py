#!/usr/bin/env python3

# auth.py

"""Authenticates user"""
from flask import request
from functools import wraps
import jwt
import os


class AuthenticationError(Exception):

    def __init__(self, errors):
        self.errors = errors


class Auth:
    _req = request
    _key = os.getenv("SECRET_KEY")

    @classmethod
    def generate_json_web_token(cls, user_id):
        return jwt.encode({"user": {"id": user_id}}, cls._key, algorithm="HS256")

    @classmethod
    def authenticate(cls, user, password):

        if not user.compare_password(password):
            raise AuthenticationError("Invalid password")
        return Auth.generate_json_web_token(user.id)

    @classmethod
    def is_authenticated(cls, func):

        @wraps(func)
        def inner_func(*args, **kwargs):
            token = cls._req.headers.get("x-auth-token", None)

            if not token:
                raise AuthenticationError("Missing header: x-auth-token")
            try:
                data = jwt.decode(token, cls._key, algorithm="HS256")
                user = data.get("user")
                user_id = user.get("id")
                if "user_id" in func.__code__.co_varnames:
                    kwargs["user_id"] = user_id
            except jwt.ExpiredSignatureError:
                raise AuthenticationError("Expired Token. Login")
            except jwt.InvalidTokenError:
                raise AuthenticationError("Token provided is Invalid.")
            return func(*args, **kwargs)
        return inner_func
