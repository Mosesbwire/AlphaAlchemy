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

from services.daily_portfolio_value import DailyPortfolioValuationService
from services.user_service import UserService
from services.stock_service import StockService
from services.stock_data_service import StockDataService
from services.portfolio_service import PortfolioService
from utils.currency.conversion import to_cents, to_unit_currency
from utils.rate_returns import return_on_investment, time_weighted_return
from datetime import datetime

stockService = StockService()
portfolioService = PortfolioService()
userService = UserService()
portfolio_id = 'be01097c-8155-4163-9702-79afa5b22c89' 
user_id =   'fde095d7-2e6a-44aa-8af3-c8f28ac83b4e' 
stock_id = 'a7257ed9-6804-460a-bd1c-a4b1b287e7c4'

if __name__ == "__main__":
    


    """      
    stock = stockService.get_stock_by_ticker("SCOM")
    """    
        
    """
    userService.create("Mose", "Bwire", "mosesbwire@gmail.com", "P@ssword1", "P@ssword1")
    """
    """
    users = userService.get_users()

    user = users[0]
    """
    """
    p = portfolioService.create(user.id, "growth-portfolio")
    
    portfolio = p.get("portfolio")
    """
    """
    portfolioService.buy_action(user_id, portfolio_id, stock_id, 100, 13.50)
    """
    """
    portfolio = portfolioService.get_portfolio_by_id(portfolio_id)
    

    mv = portfolioService.calculate_market_value(portfolio.stocks)

    """
    """ 
    service = PortfolioService()

    service.buy_action(user_id, portfolio_id, stock_id, 200, 45.50)

    details = service.get_portfolio_details(portfolio_id)

    print(details)
    """

    returns = return_on_investment(200, 250)

    print(returns)
