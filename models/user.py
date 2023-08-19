#!/usr/bin/python3

"""
    Module: user
    user class
"""


from models.base_model import BaseModel

class User(BaseModel):
    """ Class represents the User """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.first_name = args[0]
            self.last_name = args[1]
            self.email = args[2]
            self.password = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
