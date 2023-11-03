
#!/usr/bin/python3

# test_user.py

"""Test user controller actions"""
from api.v1.app import app
from controllers.users import UserController
from unittest.mock import Mock, patch
import json
import unittest


class TestUserController(unittest.TestCase):

    def test_create_action_with_invalid_data(self):
        mock_req = Mock()
        with app.app_context():
            pass
