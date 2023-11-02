
#!/usr/bin/env python3

# test_validate_data.py

"""Unittest for validate_data module"""

from utils.validate_data import validate_user_data, is_valid_email, is_valid_password
import unittest


class TestValidateData(unittest.TestCase):

    def test_is_valid_password(self):
        """test that password is inline with applications password rules"""
        with self.subTest("test validity is false if length is less than 8"):
            password = "pass"
            password2 = "passwor"
            self.assertFalse(is_valid_password(password))
            self.assertFalse(is_valid_password(password2))

        with self.subTest("test validity is false if password has no digit"):
            ps_ = "PasswordlengTh"
            self.assertFalse(is_valid_password(ps_))
        with self.subTest("test validity is false if password has no upper case"):
            ps_2 = "password1"
            self.assertFalse(is_valid_password(ps_2))
        with self.subTest("test validity is false if password has no lowercase"):
            ps_3 = "PASSWORD1"
            self.assertFalse(is_valid_password(ps_3))
        with self.subTest("test that password is valid if all rules applied"):
            ps_3 = "Password8"
            self.assertTrue(is_valid_password(ps_3))

    def test_is_valid_email(self):
        "test if email is correctly configured"
        with self.subTest("email without @ sign"):
            em = "emailgmail.com"
            self.assertFalse(is_valid_email(em))
        with self.subTest("email without domain"):
            em_ = "email@gmailcom"
            self.assertFalse(is_valid_email(em_))
        with self.subTest("email string"):
            em_1 = "emailgmailcom"
            self.assertFalse(is_valid_email(em_1))

    def test_user_registration_data_invalid_first_and_last_names(self):
        data = {"first_name": "", "last_name": "",
                "email": "email@gmail.com", "password": "Password1"}

        expected = [{"first_name": "First name cannot be empty"},
                    {"last_name": "Last name cannot be empty"}
                    ]
        actual = validate_user_data(data)

        self.assertEqual(expected, actual)
        self.assertEqual(len(actual), 2)

    def test_user_registration_data_valid(self):
        data = {"first_name": "name", "last_name": "name",
                "email": "email@gmail.com", "password": "Password1"}

        expected = []
        actual = validate_user_data(data)

        self.assertEqual(expected, actual)
        self.assertTrue(len(actual) == 0)
