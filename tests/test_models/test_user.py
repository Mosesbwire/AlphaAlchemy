#!/usr/bin/python3

"""
    Module: test_user
    Contains unittest for the user class
"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """ test class for the user class """

    def test_invalid_first_name(self):
        """test a valueError exception is raised"""

        self.assertRaises(ValueError, User, "", "lastname",
                          "email", "password", 50000)
        self.assertRaises(ValueError, User, "x", "lastname",
                          "email", "password", 50000)

    def test_invalid_last_name(self):
        """test a valueError exception is raised"""

        self.assertRaises(ValueError, User, "first", "",
                          "email", "password", 50000)
        self.assertRaises(ValueError, User, "first", "l",
                          "email", "password", 50000)

    def test_invalid_email_address(self):
        """test a valueError exception is raised"""

        self.assertRaises(ValueError, User, "name",
                          "lastname", "", "password", 50000)
        self.assertRaises(ValueError, User, "name",
                          "lastname", "email", "password", 50000)

    def test_invalid_password(self):
        """test a valueError exception is raised"""

        self.assertRaises(ValueError, User, "name", "last",
                          "email@gmail.com", "pssword")
        self.assertRaises(ValueError, User, "name", "last",
                          "email@gamil.com", "PASSWORD")
        self.assertRaises(ValueError, User, "name", "last",
                          "email@gamil.com", "password")
        self.assertRaises(ValueError, User, "name", "last",
                          "email@gamil.com", "Password")

    def test_password_is_hashed(self):
        """test that a user password is hashed"""
        password = "Password1"
        user = User("first", "last", "email@gmail.com", password)

        self.assertNotEqual(password, user.hash_password(password))

    def test_password_is_decrypted(self):
        """ test that a user password is correctly decrypted"""
        password = "Password1"
        user = User("first", "last", "email@gmail.com", password)
        self.assertTrue(user.decrypt_password(password))

    def test_balance_is_increased(self):
        """test that a user balance gets increased"""

        user = User("first", "last", "email@gmail.com", "Password1")
        new_balance = user.balance + 5000

        self.assertEqual(new_balance, user.increase_balance(5000))
        self.assertEqual(user.balance, new_balance)

    def test_balance_is_decreased(self):
        """test that a user balance is decreased"""
        user = User("first", "last", "email@gmail.com", "Password1")
        new_balance = user.balance - 5000

        self.assertEqual(new_balance, user.decrease_balance(5000))
        self.assertEqual(user.balance, new_balance)
