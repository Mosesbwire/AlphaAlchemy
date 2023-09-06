#!/usr/bin/python3

"""
    test myclasses
"""
from datetime import datetime
from decimal import Decimal
import math
import models
from models.base_model import BaseModel
from models.portfolio import Portfolio
from models.portfolio_stock import PortfolioStock
from models.stock import Stock
from models.stock_data import StockData
from models.transaction import Transaction
from models.user import User

from services.user_service import UserService
from services.stock_service import StockService
from services.stock_data_service import StockDataService
from services.portfolio_service import PortfolioService
from utils.currency.conversion import to_cents, to_unit_currency


if __name__ == "__main__":
   
    stService = StockService()
    usService = UserService()

    stock = stService.create("SCOM", "SAFARICOM", "COMMUNICATION")
    st = stService.create("EQTY", "EQUITY", "BANKING")
    user = usService.create("Mose", "Bwire", "mosesbwire@gmail.com", "P@ssword1", "P@ssword1")
    user1 = usService.create("Sheila", "Amalemba", "sheila@gmail.com", "P@ssword1", "P@ssword1")
    user2 = usService.create("Kian", "Juma", "kianjuma@gmail.com", "P@ssword1", "P@ssword1")
    """    
    USER = user.get("user")
    STOCK = stock.get("stock")
    pService = PortfolioService()
    portfolio = pService.create(USER.id,"growth-portfolio")

    PORTFOLIO = portfolio.get("portfolio")

    
    pService.buy_action(USER.id, PORTFOLIO.id, STOCK.id, 200, 12.75)
    pService.buy_action(USER.id, PORTFOLIO.id, st.get("stock").id, 100, 35.50)


    pService.buy_action(USER.id, PORTFOLIO.id, STOCK.id, 100, 12)

    pService.sell_action(USER.id, PORTFOLIO.id, STOCK.id, 200, 13.50)

    p = pService.get_portfolio_by_id(PORTFOLIO.id)
     
    print("captal invested")
    print(to_unit_currency(p.capital))

    print("current market value")

    print(pService.portfolio_market_value(p.id))


    users = usService.get_users()

    print(users)
    print(type(users[0]))
    """
