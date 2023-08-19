#!/usr/bin/python3

"""

    Module: test_transaction
    Contains unittest for the transaction class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.transaction import Transaction
import unittest


attributes = ["item", "price", "quantity", "transaction_type", "total"]

class TestTransaction(unittest.TestCase):

    """ test class for the transaction class """
    def setUp(self):
        """ instantiate transaction to be used in the tests """

        self.transaction = Transaction("ABSA", 12.00, 500, "buy", "6000.00")
        data = {
            "item": "SASINI",
            "price": 16.50,
            "quantity": 100,
            "transaction_type": "buy",
            "total": 1650.00
        }

        self.superTransaction = Transaction(**data)

    def test_is_subclass(self):
        """ test that transaction inherits from the BaseModel """

        self.assertIsInstance(self.transaction, BaseModel)
        self.assertIsInstance(self.superTransaction, BaseModel)

        self.assertTrue(hasattr(self.transaction, "id"))
        self.assertTrue(hasattr(self.transaction, "created_at"))
        self.assertTrue(hasattr(self.transaction, "updated_at"))
        self.assertTrue(hasattr(self.superTransaction, "id"))
        self.assertTrue(hasattr(self.superTransaction, "created_at"))
        self.assertTrue(hasattr(self.superTransaction, "updated_at"))

    def test_transaction_attributes_present(self):
        """ test  that all data attributes are present """
        for attr in attributes:
            with self.subTest(attr=attr):
               self.assertTrue(hasattr(self.transaction, attr))

    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.transaction.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertIn(attr, instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[Transaction] ({self.transaction.id}) {self.transaction.__dict__}"
        actual = str(self.transaction)
        self.assertEqual(expected, actual)

