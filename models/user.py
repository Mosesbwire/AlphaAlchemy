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
    balance = Column(BigInteger, nullable=False)
    portfolios = relationship("Portfolio", back_populates="user",
                              cascade="all, delete, delete-orphan")

    __DEFAULT_BALANCE: int = 50000

    def __init__(self, first_name: str, last_name: str, email: str, password: str, balance: int = __DEFAULT_BALANCE):
        """ class constructor """
        super().__init__()
        self.user_first_name = first_name
        self.user_last_name = last_name
        self.email_address = email
        self.user_password = password
        self.acc_balance = balance

    @property
    def user_first_name(self):
        return self.first_name

    @user_first_name.setter
    def user_first_name(self, name):
        if len(name) < 2:
            raise ValueError("First name must be more than 2 characters long.")
        self.first_name = name

    @property
    def user_last_name(self):
        return self.last_name

    @user_last_name.setter
    def user_last_name(self, name):
        if len(name) < 2:
            raise ValueError("Last name must be more than 2 characters long.")
        self.last_name = name

    @property
    def email_address(self):
        return self.email

    @email_address.setter
    def email_address(self, user_email):
        try:
            validators.email(user_email.strip(), allow_empty=False)
        except errors.EmptyValueError:
            raise ValueError("Email cannot be empty")
        except errors.InvalidEmailError:
            raise ValueError("Invalid email")
        else:
            self.email = user_email

    @property
    def user_password(self):
        return self.password

    @user_password.setter
    def user_password(self, user_pssword):
        password_schema = PasswordValidator()
        password_schema.min(8)\
            .max(100)\
            .has().uppercase()\
            .has().lowercase()\
            .has().digits()\
            .has().no().spaces()
        if not password_schema.validate(user_pssword):
            raise ValueError(
                "Minimum password length is 8 characters. Password must contain upper case, lower case letters and a digit.")
        self.password = self.hash_password(user_pssword)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def compare_password(self, password):
        pwd = password.encode("utf-8")
        p = bytes(str(self.user_password), "utf-8")
        if not bcrypt.checkpw(pwd, p):
            return False
        return True

    @property
    def acc_balance(self):
        return to_unit_currency(self.balance)

    @acc_balance.setter
    def acc_balance(self, bal):
        self.balance = to_cents(bal)

    def increase_balance(self, amount):
        bal = float(self.acc_balance) + amount
        self.acc_balance = bal
        return self.acc_balance

    def decrease_balance(self, amount):

        if amount > float(self.acc_balance):
            raise ValueError(
                f"Action cannot be completed. {amount} is larger that current account balance: {self.acc_balance}")
        bal = float(self.acc_balance) - amount
        self.acc_balance = bal
        return self.acc_balance

    def user_portfolio(self):
        portfolios = self.portfolios
        if not portfolios:
            return None
        return portfolios[0]

    @classmethod
    def get_user_by_email(cls, email):
        stmt = select(cls).where(cls.email == email)

        user = models.storage.query(stmt)

        if len(user) > 0:
            return user[0]

        return None

    @staticmethod
    def get_user_by_id(user_id):
        user = models.storage.get("User", user_id)
        if not user:
            return None
        return user
