#!/usr/bin/python3

"""
    Module: portfolio_service

    Contains the business logic for the Portfolio model
"""

import models
from datetime import datetime, timezone
from models.portfolio import Portfolio
from services.portfolio_stock_service import PortfolioStockService
from services.user_service import UserService
from services.stock_service import StockService
from services.transaction_service import TransactionService
from services.data_processor import DataProcessor
from utils.currency.conversion import to_cents, to_unit_currency
from utils.rate_returns import return_on_investment,time_weighted_return

dataProcessor = DataProcessor()
class PortfolioService:
    """ The PortfolioService layer contains all logic for the Portfolio """
    
    __lot_size = 100

    def __init__():
        self.current_data = dataProcessor.stocks_metrics()

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

    def calculate_market_value(self, stocks):
        """ calculates the market value of a portfolio """
        market_value = 0
        stockService = StockService()
        for stock in stocks:
            st = stockService.get_stock_by_id(stock.stock_id)
            ticker = st.ticker
            for data in self.current_data:
                if data["ticker"] == ticker:
                    market_value += (to_cents(data["current"]) * stock.quantity)

        return to_unit_currency(market_value)

    def calculate_portfolio_market_value(self, portfolio):

        market_value = self.calculate_market_value(portfolio.stocks)
        return market_value

        
    def get_portfolio_by_id(self, portfolio_id):
        """ retreives portfolio with associated portfolio_id """

        portfolio = models.storage.get("Portfolio", portfolio_id)

        if portfolio is None:
            return None

        return portfolio

    def get_portfolio_details(self, portfolio_id):
        """ returns a dict with comprehensive data on the portfolio """
        portfolio = self.get_portfolio_by_id(portfolio_id)
        if portfolio is None:
            return None
        portfolio_details = {}
        market_value = self.calculate_portfolio_market_value(portfolio)
        date_format = "%a %d %b %Y"
        today = datetime.now(timezone.utc)
        today = today.strftime(date_format)

        valuations = sorted(portfolio.valuations, key=lambda valuation: valuation.created_at)
        roi = 0
        weighted_return = 0
        if len(valuations) > 1:
            latest_valuation = valuations[-1]
            if latest_valuation.created_at.strftime(date_format) == today:
                latest_valuation = valuations[-2]

            today_transactions = list(filter(lambda transaction: transaction.created_at.strftime(date_format) == today, portfolio.transactions))
        
            net_transaction = 0

            for transaction in today_transactions:
                if transaction.transaction_type == "buy":
                    net_transaction -= transaction.total
                else:
                    net_transaction += transaction.total
        
            roi = (to_cents(market_value) - latest_valuation.portfolio_value) / latest_valuation.portfolio_value
            return_roi = (to_cents(market_value) - (latest_valuation.portfolio_value - (net_transaction)))/ (latest_valuation.portfolio_value - (net_transaction))

            weighted_return = time_weighted_return(return_roi)

        stocks = []
        stockService = StockService()
        for stock in portfolio.stocks:
            stock_detail = {}
            st = stockService.get_stock_by_id(stock.stock_id)
            stock_detail["name"] = st.name
            stock_detail["ticker"] = st.ticker
            stock_market_value = self.calculate_market_value([stock])
            stock_weight = to_cents(stock_market_value)/ to_cents(market_value)

            stock_detail["current_value"] = stock_market_value
            stock_detail["current_unit_price"] = to_unit_currency(to_cents(stock_market_value) / stock.quantity)
            stock_detail["weight"] = stock_weight
            stock_detail["quantity"] = stock.quantity

            stocks.append(stock_detail)

        portfolio_details["id"] = portfolio.id        
        portfolio_details["name"] = portfolio.name
        portfolio_details["valuation"] = market_value
        portfolio_details["roi"] = roi
        portfolio_details["returns"] = weighted_return
        portfolio_details["stocks"] = stocks

        return portfolio_details

    def get_user_portfolios(self, user_id):
        """ returns all portfolios belonging to user with given user_id """
        userService = UserService() 
        portfolios = userService.get_portfolios(user_id)
        portfolios_detailed = []

        for portfolio in portfolios:
            port = self.get_portfolio_details(portfolio.id)
            portfolios_detailed.append(port)

        return portfolios_detailed
    
    def get_portfolio_transactions(self, portfolio_id):
        """ returns the transactions of the portfolio """
        portfolio = self.get_portfolio_by_id(portfolio_id)
        if portfolio is None:
            return None

        transactions = portfolio.transactions
        return transactions

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

        transaction = transactionService.create(stock.name, stock.id, to_cents(bid_price), quantity, "buy", total_cost, portfolio)

        
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
 
        transaction = transactionService.create(stock.name, stock.id, to_cents(ask_price), quantity, "sell", total_revenue, portfolio)

        user.balance = user.balance + total_revenue

        models.storage.save()

        return {"transaction": transaction.get("transaction"), "error": None}

