#!/usr/bin/env python3

# validate_data.py

"""Functonality used to validate data"""
from password_validator import PasswordValidator
from validator_collection import validators, checkers, errors


def is_valid_password(password):
    """ checks that password adheres to password rules"""
    password_schema = PasswordValidator()
    password_schema.min(8)\
        .max(100)\
        .has().uppercase()\
        .has().lowercase()\
        .has().digits()\
        .has().no().spaces()
    return password_schema.validate(password)


def is_valid_email(email):
    """checks that email address is correctly configured"""
    try:
        validators.email(email.strip(), allow_empty=False)
    except errors.InvalidEmailError:
        return False
    return True


def validate_user_data(data):
    """Checks that data provided by client is valid
        Args:
            data: data from client
        Returns:
            empty list []: if all data valid
            list[{error}]: list with errors
    """

    error = []
    try:
        validators.string(
            data.get("first_name").strip(), allow_empty=False, minimum_length=1)
    except errors.EmptyValueError as e:
        error.append({"first_name": "First name cannot be empty"})

    try:
        validators.string(
            data.get("last_name").strip(), allow_empty=False, minimum_length=1)
    except errors.EmptyValueError as e:
        error.append({"last_name": "Last name cannot be empty"})

    if not is_valid_password(data.get("password")):
        error.append(
            {"password": "Password must minimum length is 8 characters and must containe uppercase letter, lowercase letter and at least one digit."})

    if not is_valid_email(data.get("email")):
        error.append({"email": "Incorrect email format"})

    return error
