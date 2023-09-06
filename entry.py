#!/usr/bin/python3


from services.data_processor import DataProcessor


if __name__ == "__main__":
    

    p = DataProcessor()

    data = p.market_metrics()


    
    print(data)
