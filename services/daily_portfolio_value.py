#!/usr/bin/python3

import models

from models.daily_portfolio_valuation import DailyPortfolioValuation
from services.portfolio_service import PortfolioService
from utils.currency.conversion import to_cents, to_unit_currency

class DailyPortfolioValuationService:

   
    def create(self, valuation,portfolio):

        daily_valuation = DailyPortfolioValuation(to_cents(valuation))
        portfolio.valuations.append(daily_valuation)

        models.storage.new(daily_valuation)
        models.storage.save()

    def scheduled_portfolio_valuation_job(self):
        portfolioService = PortfolioService()

        portfolios = models.storage.all("Portfolio")

        for portfolio in portfolios:
            valuation = portfolioService.calculate_portfolio_market_value(portfolio)

            self.create(valuation, portfolio)
