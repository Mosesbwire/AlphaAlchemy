#!/usr/bin/python3

"""

    Module: test_transaction
    Contains unittest for the transaction class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.transaction import Transaction
import unittest


class TestTransaction(unittest.TestCase):

    """ test class for the transaction class """

    def test_error_raised_on_incorrect_price(self):
        """test ValueError is raised if price is incorrect"""

        self.assertRaises(ValueError, Transaction, "SCOM", 0, 100, "buy")

    def test_error_raised_on_incorrect_quantity(self):
        """test value error is raised if quantity is incorrect"""
        self.assertRaises(ValueError, Transaction, "KCB", 23, 0, "sell")

    def test_error_raised_on_incorrect_transaction_type(self):
        """test value error is raised if transaction type is incorrect"""
        self.assertRaises(ValueError, Transaction, "NMG", 23, 100, "UNKNONW")
