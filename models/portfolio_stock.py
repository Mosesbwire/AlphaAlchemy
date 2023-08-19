#!/usr/bin/python3

"""
    Module: portfolio_stock
    PortfolioStock class
"""


from models.base_model import BaseModel

class PortfolioStock(BaseModel):
    """ 
        Class represents a stock in aportfolio

    """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()
        if args:
            self.quantity = args[0]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
