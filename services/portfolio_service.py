#!/usr/bin/python3

"""
    Module: portfolio_service

    Contains the business logic for the Portfolio model
"""

import models
from models.portfolio import Portfolio
from services.portfolio_stock_service import PortfolioStockService
from services.user_service import UserService
from services.stock_service import StockService
from services.transaction_service import TransactionService
from utils.currency.conversion import to_cents, to_unit_currency

class PortfolioService:
    """ The PortfolioService layer contains all logic for the Portfolio """
    
    __lot_size = 100

    def create(self, user_id, name = None):
        """ create a portfolio """
        userService =  UserService()

        user = userService.get_user_by_id(user_id)

        if user is None:
            msg = f"User with id: {user_id} not found"
            return {"portfolio": None, "error": [msg]}

        if name is None:
            name = "Investment Portfolio"

        portfolio = Portfolio(name = name)

        if not portfolio:
            return {"portfolio": None, "error": ["Failed to create portfolio"]}

        user.portfolios.append(portfolio)

        models.storage.save()

        return {"portfolio": portfolio, "error": None}

    def get_portfolio_by_id(self, portfolio_id):
        """ retreives portfolio with associated portfolio_id """

        portfolio = models.storage.get("Portfolio", portfolio_id)

        if portfolio is None:
            return None

        return portfolio

    def get_user_portfolios(self, user_id):
        """ returns all portfolios belonging to user with given user_id """
        userService = UserService()
        portfolios = userService.get_portfolios(user_id)

        return portfolios
    
    def buy_action(self, user_id, portfolio_id, stock_id, quantity, bid_price):
        """ add stocks to a users portfolio """
        userService = UserService()
        transactionService = TransactionService()
        portfolioStockService = PortfolioStockService()
        stockService = StockService()

        user = userService.get_user_by_id(user_id)

        if user is None:
            return {"transaction": None, "error": {"status": 404, "message": "User not found"}}
             
        if user.balance < (to_cents(bid_price) * quantity):
            err_message = f"Your account has insufficient funds to complete the transaction. Balance: {to_unit_currency(user.balance)} Transaction {bid_price * quantity}"
            return {"transaction": None, "error": {"status": 400, "message": err_message}}

        portfolio = self.get_portfolio_by_id(portfolio_id)

        if portfolio is None:
            return {"transaction": None, "error": {"status": 404, "message": "Portfolio not found"}}

        stock = stockService.get_stock_by_id(stock_id)

        if stock is None:
            return {"transaction": None, "error": {"status": 404, "message": "Stock not found"}}

        if stock.status != "active":
            err_message = f"{stock.name}'s shares can not be traded. It has been {stock.status}."
            return {"transaction": None, "error": {"status": 400, "message":  err_message}}
        
        if quantity % self.__lot_size != 0:
            err_message = f"Shares can only be bought in multiples of 100: {quantity}"
            return {"transaction": None, "error":{"status": 400, "message":err_message}}

        if bid_price <= 0:
            err_message = f"Bid price can not be 0 or negative value: {bid_price}"
            return {"transaction": None, "error": {"status": 400, "message": err_message}}

        total_cost = to_cents(bid_price) * quantity

        user.balance = user.balance - total_cost

        portfolio.capital = portfolio.capital + total_cost
        
        portfolioStock = None
        isStockPresent = False

        if len(portfolio.stocks) > 0:
            for st in portfolio.stocks:
                if st.stock_id == stock_id:
                    st.quantity = st.quantity + quantity
                    isStockPresent = True
                    break
            if not isStockPresent:
                portfolioStock = portfolioStockService.create(quantity, portfolio, stock)
        else:
            portfolioStock = portfolioStockService.create(quantity, portfolio, stock)

        

        transaction = transactionService.create(stock.name, to_cents(bid_price), quantity, "buy", total_cost, portfolio)

        
        models.storage.save()

        return {"transaction": transaction.get("transaction"), "error": None}

    def sell_action(self, user_id, portfolio_id, stock_id, quantity, ask_price):
        """ sells the specified quantity from a portfolio """
        userService = UserService()
        transactionService = TransactionService()
        portfolioStockService = PortfolioStockService()
        stockService = StockService()

        user = userService.get_user_by_id(user_id)

        if user is None:
            return {"transaction": None, "error": {"status": 404, "message": "User not found"}}

        portfolio = self.get_portfolio_by_id(portfolio_id)

        if portfolio is None:
            return {"transaction": None, "error": {"status": 404, "message": "Portfolio not found"}}

        stock = stockService.get_stock_by_id(stock_id)

        if stock is None:
            return {"transaction": None, "error": {"status": 404, "message": "Stock not found"}}

        if stock.status != "active":
            err_message = f"{stock.name}'s shares can not be traded. It has been {stock.status}."
            return {"transaction": None, "error": {"status": 400, "message":  err_message}}
        
        if quantity % self.__lot_size != 0:
            err_message = f"Shares can only be bought in multiples of 100: {quantity}"
            return {"transaction": None, "error":{"status": 400, "message":err_message}}
        
        isStockPresent = False

        for st in portfolio.stocks:
            if st.stock_id == stock_id:
                if quantity > st.quantity:
                    err_message = f"Invalid transaction. Quantity being sold {quantity} is greater than quantity owned {st.quantity}"
                    return {"transaction": None, "error": {"status": 400, "message": err_message}}
                st.quantity = st.quantity - quantity
                isStockPresent = True
                break
        if not isStockPresent:
            err_message = f"Invalid Transaction. Transaction cannot be completed Stock {stock.name} is not in your portfolio."
            return {"transaction": None, "error": {"status": 400, "message": err_message}}
        
        total_revenue = to_cents(ask_price) * quantity
 
        transaction = transactionService.create(stock.name, to_cents(ask_price), quantity, "sell", total_revenue, portfolio)

        user.balance = user.balance + total_revenue

        models.storage.save()

        return {"transaction": transaction.get("transaction"), "error": None}

    def portfolio_market_value(self, portfolio_id):
        stockService = StockService()
        portfolio = self.get_portfolio_by_id(portfolio_id)
        data = stockService.fetch_latest_prices()
        market_value = 0

        for stock in  portfolio.stocks:
            
            price = stockService.current_price(stock.stock.ticker, data)

            value = to_cents(price) * stock.quantity

            market_value += value

        return to_unit_currency(market_value)
        
