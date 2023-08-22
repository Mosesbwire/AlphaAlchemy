#!/usr/bin/python3

"""
    Module: test_user_service

    This module contains unittests for the UserService class
"""

import bcrypt
import models
import services
from services.user_service import UserService
import unittest
from unittest.mock import Mock


class TestUserService(unittest.TestCase):
    """ contains unittest for the UserService class """

    def setUp(self):
        """ init an instance of UserService to be used in the tests """

        self.userService = UserService()

    def tearDown(self):
        """ clears all resources used after running each test """
        pass


    def test_instance_initialized_correctly(self):
        """ test that instance initialized correctly """

        self.assertIsInstance(self.userService, UserService)

    def test_create_function_return_dict(self):
        """ test that create returns a dictionary """
        data = self.userService.create("User", "username", "username@gmail.com", "P@ssword1", "P@ssword1")

        self.assertIsInstance(data, dict)
        self.assertEqual(len(data.keys()), 2)

    def test_create_function_return_dict_with_user(self):
        """ test that returned dict has user key"""
        data = self.userService.create("User", "username", "username@gmail.com", "P@ssword1", "P@ssword1")
        self.assertIn("user", data)

    def test_create_function_return_dict_with_error(self):
        """ test validations in create function return error messages """
        data = self.userService.create("User", "username", "username@gmail.com", "P@ssword1", "P@ssword1")
        self.assertIn("error", data)
    
    def test_validation_error_for_empty_names(self):
        """ test that error is generated if names are empty """
        expected_error_msg = ["First name cannot be empty", "Last name cannot be empty"]

        badData = self.userService.create("", "", "email", "password", "cpassword")
        error = badData.get("error")

        for idx, expected in enumerate(expected_error_msg):
            with self.subTest(expected = expected):
                self.assertEqual(error[idx], expected)
    
    def test_validation_error_for_invalid_email_syntax(self):
        """ test that error is generated if email syntax is incorrect """
        badData = self.userService.create("first", "last", "email", "password", "cpassword")

        expected_error_msg = "Email format is incorrect"
        err = badData.get("error")

        self.assertEqual(err[0], expected_error_msg)

    def test_validation_error_for_invalid_password_format(self):
        """ test that error is generated if password format fails validation """
        
        expected_err_msg = "Password must be more than 6 characters long.\n\
                Password should have atleast 1 uppercase letter.\n\
                Password should have atleast 1 digit.\n\
                Password should have atleast 1 symbol."

        weak1 = self.userService.create("first", "last", "firstlast@gmail.com", "password", "password")
        weak2 = self.userService.create("first", "last", "firstlast@gmail.com", "Password1", "Password1")
        weak3 = self.userService.create("first", "last", "firstlast@gmail.com", "Password_", "Password_")
        weak = self.userService.create("first", "last", "firstlast@gmail.com", "Password", "Password")

        self.assertEqual(expected_err_msg, weak1.get("error")[0])
        self.assertEqual(expected_err_msg, weak2.get("error")[0])
        self.assertEqual(expected_err_msg, weak3.get("error")[0])
        self.assertEqual(expected_err_msg, weak.get("error")[0])

    def test_user_is_none_on_error(self):
        """ test that user is None if error has occured """

        data = self.userService.create("", "last", "email", "pwd", "pwd")

        self.assertIsNone(data.get("user"))

    def test_user_is_returned_on_valid_data(self):
        """ test a valid user is returned when valid data is passed """

        data = self.userService.create("first", "last", "first@gmail.com", "P@ssword1", "P@ssword1")

        self.assertIsNotNone(data.get("user"))
    
    def test_password_is_hashed(self):
        """ test that password is hashed on save """

        data = self.userService.create("first", "last", "first@gmail.com", "P@ssword1", "P@ssword1")

        user = data.get("user")

        self.assertNotEqual(user.password, "P@ssword1")
        self.assertTrue(bcrypt.checkpw("P@ssword1".encode('utf-8'), user.password))
                
    def test_function_get_by_id_returns_user(self):
        """ test that user is returned """

        data = self.userService.create("first", "last", "first@gmail.com", "P@ssword1", "P@ssword1")
        user = data.get("user")

        fetchedUser = self.userService.get_user_by_id(user.id)

        self.assertIs(user, fetchedUser)
        self.assertEqual(user.id, fetchedUser.id)

    def test_function_get_by_id_returns_none(self):
        """ test that None is returned when invalid id is passed """

        user = self.userService.get_user_by_id("120")

        self.assertIsNone(user)


    def test_function_get_users(self):
        """ test that a list of users is returned """


        self.userService.create("first", "last", "First@gmail.com", "P@ssword1", "P@ssword1")
        self.userService.create("first", "last", "irst@gmail.com", "P@ssword1", "P@ssword1")
        self.userService.create("first", "last", "Lirst@gmail.com", "P@ssword1", "P@ssword1")
        users = self.userService.get_users()

        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 3)
    
        
    def test_fuction_get_users_return_empty_list(self):
        """ test that an empty list is returned if there is no data in database """

        users = self.userService.get_users()

        self.assertEqual(len(users), 0)
        self.assertIsInstance(users, list)

    def test_delete_function(self):
        """ test that user get deleted """
        data = self.userService.create("User", "Usr", "user@gmail.com", "P@ssword1", "P@ssword1")

        user = data.get("user")
        id = user.id
        status = self.userService.delete_user(id)
        fetchedUser = self.userService.get_user_by_id(id)

        self.assertEqual(status, "ok")
        self.assertIsNone(fetchedUser)

    def test_update_function_returns_dict(self):
        """ test that return value is a dict """

        data = self.userService.create("User", "Usr", "user@gmail.com", "P@ssword1", "P@ssword1")
        user = data.get("user")
        first_name = "NEW"
        last_name = "UPDATED"

        user_data = self.userService.update_user(user.id, first_name = first_name, last_name = last_name)

        self.assertIsInstance(user_data, dict)

        self.assertIn("user", user_data)
        self.assertIn("error", user_data)

    def test_update_function(self):
        """ test the user data is updated """ 
        data = self.userService.create("User", "Usr", "user@gmail.com", "P@ssword1", "P@ssword1")
        user = data.get("user")
        first_name = "NEW"
        last_name = "UPDATED"
        

        user_data = self.userService.update_user(user.id, first_name = first_name, last_name = last_name)
        u = user_data.get("user")

        self.assertIs(user, u)
        self.assertEqual(u.first_name, first_name)
        self.assertEqual(u.last_name, last_name)
        self.assertNotEqual(u.updated_at, user.updated_at)

    def test_update_function_returns_none(self):
        """ return None if user does not exist """

        user_data = self.userService.update_user("21", first_name= "Name")
        user = user_data.get("user")
        error = user_data.get("error")

        self.assertIsNone(user)
        self.assertEqual(len(error), 0)

    def test_update_function_returns_error_on_validation_fails(self):
        """ return error if validations fail """
        
        data = self.userService.create("User", "Usr", "user@gmail.com", "P@ssword1", "P@ssword1")
        user = data.get("user")
        first_name = ""
        last_name = ""
        user_data = self.userService.update_user(user.id, first_name = first_name, last_name = last_name)

        expected_error_msg = ["First name cannot be empty", "Last name cannot be empty"]

        error = user_data.get("error")

        for idx, err in enumerate(expected_error_msg):
            with self.subTest(err = err):
                self.assertEqual(error[idx], err)








