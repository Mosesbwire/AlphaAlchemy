#!/usr/bin/python3

"""
    module storage:
    Contains the class that provides a connection and manipulates the database
"""

import models
from models.base_model import BaseModel, Base
from models.portfolio import Portfolio
from models.portfolio_stock import PortfolioStock
from models.stock import Stock
from models.stock_data import StockData
from models.transaction import Transaction
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
        "Portfolio": Portfolio,
        "PortfolioStock": PortfolioStock,
        "Stock": Stock,
        "StockData": StockData,
        "Transaction": Transaction,
        "User": User
}

class Storage:
    """ Provides the connection between the application and the database """
    __engine = None
    __session = None

    def __init__(self, dburl):
        """ constructor """
        self.__engine = create_engine(dburl)

        ENV = "test"

        if ENV == "test":
            Base.metadata.drop_all(self.__engine)
    
    def reset(self):
        self.__session.rollback()

    def new(self, obj):
        """ adds a object to the session """
        self.__session.add(obj)


    def save(self):
        """ saves objects in the current session to the database """
        self.__session.commit()


    def delete(self, obj=None):
        """ deletes object from the current database session """

        if obj is not None:
            self.__session.delete(obj)

    def roll_back(self):
        """ reverts an object in session to its previous state if save has not been called """
        self.__session.rollback()


    def close(self):
        """ closes the current database session """
        self.__session.remove()
    
    def all(self, cls):
        """ returns all objects that are instances of cls """
        if cls not in classes:
            return None
        return self.__session.query(classes[cls]).all()

    def get(self, cls, id):
        """ retrive object by class and id from the database """
        if cls not in classes:
            return None
        return self.__session.get(classes[cls], id)


    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind = self.__engine, expire_on_commit = False)
        Session = scoped_session(session_factory)
        self.__session = Session

