#!/usr/bin/python3


from services.stock_service import StockService

service = StockService()

service.fetch_stocks()
