#!/usr/bin/python3

"""
    Module: transaction
    Transaction class
"""


from models.base_model import BaseModel

class Transaction(BaseModel):
    """ 
        Class represents a transactio carried out by user on given  portfolio

    """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            self.item = args[0]
            self.price = args[1]
            self.quantity = args[2]
            self.transaction_type = args[3]
            self.total = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
