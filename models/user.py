#!/usr/bin/python3

"""
    Module: user
    user class
"""
import bcrypt
import models
from models.base_model import BaseModel, Base
from password_validator import PasswordValidator
from sqlalchemy import BigInteger, Column, String, select
from sqlalchemy.orm import relationship
from utils.currency.conversion import to_cents, to_unit_currency
from validator_collection import validators, errors


class User(BaseModel, Base):
    """ Class represents the User """
    __tablename__ = "users"

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    balance = Column(BigInteger, default=5000000, nullable=False)
    portfolios = relationship("Portfolio", back_populates="user",
                              cascade="all, delete, delete-orphan")

    __DEFAULT_BALANCE: int = 50000

    def __init__(self, first_name: str, last_name: str, email: str, password: str, balance: int = __DEFAULT_BALANCE):
        """ class constructor """
        super().__init__()
        self._first_name = None
        self._last_name = None
        self._email = None
        self._password = None
        self._balance = None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.balance = balance

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if (len(first_name) < 2):
            raise ValueError("First name must be more than 2 characters long.")
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if (len(last_name) < 2):
            raise ValueError("Last name must be more than 2 characters long.")
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        try:
            validators.email(email.strip(), allow_empty=False)
        except errors.EmptyValueError:
            raise ValueError("Email cannot be empty")
        except errors.InvalidEmailError:
            raise ValueError("Invalid email")
        else:
            self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        password_schema = PasswordValidator()
        password_schema.min(8)\
            .max(100)\
            .has().uppercase()\
            .has().lowercase()\
            .has().digits()\
            .has().no().spaces()
        if not password_schema.validate(password):
            raise ValueError(
                "Minimum password length is 8 characters. Password must contain upper case, lower case letters and a digit.")
        self._password = self.hash_password(password)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def decrypt_password(self, password):
        if not bcrypt.checkpw(password.encode("utf-8"), self.password):
            return False
        return True

    @property
    def balance(self):
        return to_unit_currency(self._balance)

    @balance.setter
    def balance(self, balance):
        self._balance = to_cents(balance)

    def increase_balance(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def decrease_balance(self, amount):
        self.balance = self.balance - amount
        return self.balance

    @classmethod
    def get_user_by_email(cls, email):
        stmt = select(cls).where(cls.email == email)

        user = models.storage.query(stmt)

        if len(user) > 0:
            return user[0]

        return None
