#!/usr/bin/python3

"""
    Module: portfolio
    Portfolio class
"""


from models.base_model import BaseModel

class Portfolio(BaseModel):
    """ 
        Class represents a users portfolio

    """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        self.status = "open"
        if args:
            self.name = args[0]
            self.capital = args[1]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
