#!/usr/bin/python3

import models

from models.portfolio_stock import PortfolioStock


class PortfolioStockService:

    def create(self, quantity, portfolio, stock):

        portfolioStock = PortfolioStock(quantity)

        portfolioStock.stock = stock

        portfolio.stocks.append(portfolioStock)
        
        return {"stock": stock, "error": None}

