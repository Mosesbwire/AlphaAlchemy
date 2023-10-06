#!/usr/bin/python3

from services.daily_portfolio_value import DailyPortfolioValuationService
from services.stock_data_service import StockDataService
import schedule
import time

dataService = StockDataService()
valuationService = DailyPortfolioValuationService()


schedule.every().day.at("17:00").do(dataService.add_daily_stock_data)
schedule.every().day.at("17:05").do(valuationService.scheduled_portfolio_valuation_job)


if __name__ == "__main__":
    while True:   
        print("Running")
        schedule.run_pending()
        time.sleep(1)
        
