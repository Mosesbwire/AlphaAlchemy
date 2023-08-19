#!/usr/bin/python3

"""
    Module: stock_data
    StockData class
"""


from models.base_model import BaseModel

class StockData(BaseModel):
    """ 
        Class represents individual data points at given times
        Data points show market activity for the given stock at given time
    """

    def __init__(self, *args, **kwargs):
        """ class constructor """
        super().__init__()

        if args:
            self.prev = args[0]
            self.current = args[1]
            self.price_change = args[2]
            self.percentage_price_change = args[3]
            self.high = args[4]
            self.low = args[5]
            self.volume = args[6]
            self.average = args[7]
            self.time = args[8]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
