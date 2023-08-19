#!/usr/bin/python3

"""
    Module: test_user
    Contains unittest for the user class
"""

from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import unittest

class TestUser(unittest.TestCase):
    """ test class for the user class """
    def setUp(self):
        """ instantiate a user to be used in the tests """

        self.user = User("user","super", "user@gmail.com", "password")
        data = {
            "first_name": "super",
            "last_name": "user",
            "email": "superuser@gmail.com",
            "password": "password"
        }

        self.superUser = User(**data)

    def test_is_subclass(self):
        """ test that user inherits from the BaseModel """

        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.superUser, BaseModel)

        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.superUser, "id"))
        self.assertTrue(hasattr(self.superUser, "created_at"))
        self.assertTrue(hasattr(self.superUser, "updated_at"))

    def test_name(self):
        """ test that user has attribute first_name, last_name"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertTrue(hasattr(self.superUser, "first_name"))
        self.assertTrue(hasattr(self.superUser, "last_name"))

    def test_email(self):
        """ test user has attribute email """

        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.superUser, "email"))

    def test_password(self):
        """ test user has attribute password """
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.superUser, "password"))
    
    def test_to_dict(self):
        """ test the to dict function returns a dictionary with correct attr """

        instance_dict = self.user.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertIn("first_name", instance_dict)
        self.assertIn("last_name", instance_dict)
        self.assertIn("email", instance_dict)
        self.assertIn("password", instance_dict)
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_str(self):
        """ test __str__ returns expected string format """

        expected = f"[User] ({self.user.id}) {self.user.__dict__}"
        actual = str(self.user)

        self.assertEqual(expected, actual)

