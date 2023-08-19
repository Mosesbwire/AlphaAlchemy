#!/usr/bin/python3

"""
    Module: stock
    stock class
"""


from models.base_model import BaseModel

class Stock(BaseModel):
    """ Class represents the each individual stock in the stock exchange """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.ticker = args[0]
            self.name = args[1]
            self.sector = args[2]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
