import requests
import pandas as pd


def create_stock_dataframe(ticker="NONE", size="full"):
    if ticker == "NONE":
        return None

    function = 'function=TIME_SERIES_DAILY'
    symbol = f'symbol={ticker}'
    size = f'outputsize={size}'
    api_key = 'apikey=C0S1BTKMMN5286JT'
    url = f'https://www.alphavantage.co/query?&{function}&{symbol}&{size}&{api_key}'

    response = requests.get(url)
    json_stock_data = response.json()

    if 'Error Message' in json_stock_data:
        raise ValueError(f'Invalid API call for ticker {ticker}')

    df = pd.DataFrame.from_dict(json_stock_data['Time Series (Daily)'], orient='index')

    return df


class Stock:
    def __init__(self, ticker):
        self.__ticker = ticker
        self.__dataframe = create_stock_dataframe(ticker)

    def get_ticker(self):
        return self.__ticker

    def get_dataframe(self):
        return self.__dataframe

    def get_returns(self):
        stock_returns = pd.to_numeric(self.__dataframe['4. close']) - pd.to_numeric(self.__dataframe['1. open'])
        return stock_returns

