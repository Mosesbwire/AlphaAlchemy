#!/usr/bin/python3

import models

from models.daily_portfolio_valuation import DailyPortfolioValuation
from utils.currency.conversion import to_cents, to_unit_currency

class DailyPortfolioValuationService:

    def create(self, valuation,portfolio):

        daily_valuation = DailyPortfolioValuation(to_cents(valuation))
        portfolio.valuations.append(daily_valuation)

        models.storage.new(daily_valuation)
        models.storage.save()
