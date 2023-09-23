#!/usr/bin/python3
""" Module: user_service
    contains the user service class
"""
import bcrypt
from datetime import datetime, timezone
import models
from models.user import User
from password_validator import PasswordValidator
from validator_collection import validators, checkers, errors

class UserService:
    """ UserService class 
        Encaspulates the business logic associated with the User model
    """
    
    def create(self, first_name, last_name, email, password, confirm_password):
        """ creates instance of a User Model 

            Args:
                first_name: user's first name
                last_name: user's last name
                email: user's email
                password: secure account password
                confirm_password: should be equal to password

            Returns:
                dict: contains user and error
                    user if execution was successful otherwise None
                    error if execution fails otherwise empty array
        """
        error = []

        passwordSchema = PasswordValidator()

        passwordSchema.min(6)\
                .max(100)\
                .has().uppercase()\
                .has().lowercase()\
                .has().digits()\
                .has().no().spaces()\
                .has().symbols()

        try:
            first_name = validators.string(first_name.strip(), allow_empty = False, minimum_length = 1)
        except errors.EmptyValueError as e:
            error.append({"first_name":"First name cannot be empty"})

        try:
            last_name = validators.string(last_name.strip(), allow_empty = False, minimum_length = 1)
        except errors.EmptyValueError as e:
            error.append({"last_name":"Last name cannot be empty"})

        try:
            email = validators.email(email.strip(), allow_empty = False)
        except errors.EmptyValueError as e:
            error.append({"email":"Email cannot be empty"})
        except errors.InvalidEmailError as e:
            error.append({"email":"Email format is incorrect"})


        if not passwordSchema.validate(password):
            error.append({"password": "Length must be more than 6 characters, have 1 alphabet, 1 special character and 1 digit"})

        if password != confirm_password:
            error.append({"password":"Confirm password must be equal to password"})

        if len(error) != 0:
            return {"user": None, "error": error}

        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password.encode('utf-8') ,salt)

        user = User(first_name, last_name, email, hashed_password)

        if not user:
            return {"user": None, error: ["Failed to create user"] }

        try:
            models.storage.new(user)
        except Exception as e:
            print(f"Error occured: {e}")
            user = None
            error = [e]
        else:
            models.storage.save()

        return {"user": user, "error": error}


    def get_user_by_id(self, id):
        """ retrieves user by id from the database

        Args:
            id: parameter to use to fetch user from the database
        Returns:
            user: if user with id exists
            None: if no user with id exists
        """
        user = None
        try:
            user = models.storage.get("User", id)
            return user
        except Exception as e:
            print (f"Error occured: {e}")

        return user

    def get_user_by_email(self, email):
        """ retrives user by email from database
        Args:
            email: users email
        Returns:
            user: if user with email exists
            None: if no user with email
        """
        try:
            user = User.get_user_by_email(email)
            return user
        except Exception as e:
            print(f"Error occured: {e}")

        return None

    def get_users(self):
        """ retrieves all users from database 

            Returns:
                list
        """
        
        users = None
        try:
            users = models.storage.all("User")
        except Exception as e:
            print(f"Error occured: {e}")
        
        return users
    
    def delete_user(self, id):
        """ delete user from database
            Args:
                id: id of user to be deleted
            Returns:
                None: if user does not exists
                ok: if user is deleted
        """
        user = self.get_user_by_id(id)

        if user is None:
            return None

        try:
            models.storage.delete(user)
        except Exception as e:
            print(f"Error occured: {e}")
        else:
            models.storage.save()

        return "ok"
    
    def update_user(self, user_id, first_name=None, last_name=None):
        """ updates the user data

            Args:
                user_id: id for user to update data
                kwargs: user attributes to update
            Returns:
                dict
                    {user: user, error: []}
                if error
        """

        user = self.get_user_by_id(user_id)
        error = []

        if user is None:
            return {"user": None, "error": error}
        
        
        if first_name is not None:
            try:
                first_name = validators.string(first_name, allow_empty = False, minimum_length = 1)
            except errors.EmptyValueError as e:
                error.append("First name cannot be empty")

        if last_name is not None:
            try:
                last_name = validators.string(last_name, allow_empty = False, minimum_length = 1)
            except errors.EmptyValueError as e:
                error.append("Last name cannot be empty")

        if len(error) != 0:
            return {"user": None, "error": error}

        
        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        user.updated_at = datetime.now(timezone.utc)

        try:
            models.storage.save()
        except Exception as e:
            """ roll back if exception """
            user = None
            error = [e]

        return {"user": user, "error": error}

    def get_portfolios(self,user_id):
        """ get the all the users portfolio """
        portfolios = User.get_portfolios(user_id)
        data = []
        for portfolio in portfolios:
            stocks = portfolio.stocks  
            data.append(portfolio)

        return data
