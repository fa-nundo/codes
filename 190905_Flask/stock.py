import pandas as pd
import datetime as dt
from pandas_datareader import data
import pandas_datareader as pdr

def get_csv(company):
    start = dt.datetime(2016, 12, 31)
    end = dt.datetime.now()

    stocks = pdr.get_data_yahoo(company, start=start, end=end)
    stocks.to_csv(r'data/export.csv', index = None, header=True)
    return stocks

def get_csv_html(company):
    start = dt.datetime(2016, 12, 31)
    end = dt.datetime.now()

    stocks = pdr.get_data_yahoo(company, start=start, end=end)
    stocks.to_csv(r'data/export.csv', index = True, header=True)
    stocks = pd.read_csv('data/export.csv').to_html()
    return stocks

#stocks.to_csv(r'/Users/Florent/Desktop/190905 Flask/data/export_dataframe.csv', index = None, header=True)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from IPython.display import display_html
import matplotlib.pyplot as plt  
    
def get_csv_scrap_btc():
    # Date parameters
    start_date = '20170101'
    end_date = '20190930'

    # Web scrapping on https://coinmarketcap.com
    url = f'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start={start_date}&end={end_date}'
    r = requests.get(url)
    bitcoin = BeautifulSoup(r.text, 'lxml')

    # Data preparation
    bitcoin = bitcoin.find_all('table', class_='table')[0]
    html_bitcoin = str(bitcoin)
    bitcoin_stocks = pd.read_html(html_bitcoin)[0]
    
    bitcoin_stocks = pd.DataFrame(bitcoin_stocks)
    bitcoin_stocks['Date'] = pd.to_datetime(bitcoin_stocks['Date'])
    
    return bitcoin_stocks

#bitcoin_stocks = get_csv_scrap_btc()
#plt.plot(bitcoin_stocks['Date'], bitcoin_stocks['High'])
    
def get_csv_gold():
    # Get monthly gold price
    gold_stocks = pd.read_csv('https://datahub.io/core/gold-prices/r/monthly.csv')
    gold_stocks = pd.DataFrame(gold_stocks)
    gold_stocks['Date'] = pd.to_datetime(gold_stocks['Date'])
    return gold_stocks

#gold_stocks = get_csv_gold()
#gold_stocks_2017 = gold_stocks[gold_stocks['Date'] > '2016-12-01']
#plt.plot(gold_stocks_2017['Date'], gold_stocks_2017['Price'])

def get_html_realestate():
    realestate_stocks = pd.read_html('data/190905_RealEstateData.html')[0]
    realestate_stocks = pd.DataFrame(realestate_stocks)
    realestate_stocks['Date'] = pd.to_datetime(realestate_stocks['Date'])
    
    return realestate_stocks

#realestate_stocks = get_html_realestate()
#print(realestate_stocks.dtypes)
#plt.plot(realestate_stocks['Date'], realestate_stocks['High'])