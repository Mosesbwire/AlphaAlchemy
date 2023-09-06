#!/usr/bin/python3

class BadRequest(Exception):

    def __init__(self, errors):
        self.errors = errors


class AuthenticationFailed(Exception):

    def __init__(self, errors):
        self.errors = errors
