#!/usr/bin/env python3

from models.user import User
from models.portfolio import Portfolio
from models.portfolio_stock import PortfolioStock
from models.stock import Stock
from models.transaction import Transaction
from services.fetch_data import FetchData
import timeit

if __name__ == "__main__":
    # user = User("Kian", "Juma", "kianjuma@gmail.com", "Password1")

    # portfolio = Portfolio()

    # user.portfolios.append(portfolio)

    st_1 = Stock.get_stock_by_ticker("EQTY")
    st_2 = Stock.get_stock_by_ticker("SCOM")
    st_3 = Stock.get_stock_by_ticker("KCB")

    # for i in [st_1, st_2]:
    #     ps = PortfolioStock(200, i, portfolio)
    #     ps.create()

    # user.save()

    user = User.get_user_by_email("kianjuma@gmail.com")

    portfolio = user.portfolios[0]

    # ps = portfolio.buy_stock(100, 100, st_1)
    # ps = portfolio.buy_stock(45.50, 100, st_3)
    # ps = portfolio.sell_stock(110, 100, st_1)
    stock_data = FetchData.get_stock_action()
    details = portfolio.portfolio_details(stock_data)

    print(details)
