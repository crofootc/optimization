from stock import Stock
import pandas as pd

class Portfolio:
    def __init__(self):
        self.__portfolio = {}
        self.__portfolio_size = 0

    def add_stock(self, stock):
        self.__portfolio[stock.get_ticker()] = stock
        self.__portfolio_size += 1

    def remove_stock(self, ticker):
        if ticker not in self.__portfolio:
            raise ValueError(f'Stock {ticker} is not in portfolio')
        self.__portfolio_size -= 1
        del self.__portfolio[ticker]

    def get_return_dataframe(self):
        return_data = pd.DataFrame
        for i in self.__portfolio:



