from vnstock import Quote
from datetime import date, timedelta
from typing import Iterable, Optional
import pandas as pd

'''
FETCH_INFO
    This library is use to fetch and validate info from the vnstock library

'''

def fetch_stock(tickers: Iterable[str], hist: int, end_date: Optional[str] = None, combine: Optional[bool] = False):
    '''
    Docstring for fetch_stock:
    :param ticker: Takes in an array/iterable of tickers (array will suffice)
    :type ticker: Iterable str
    :param hist: Takes in an int number of days to get for historical
    :type hist: int
    :end_date: Optional, takes in a datetime string in isoformat [YYYY-MM-DD], default is today
    :type end_date: str
    :param combine: Optional, whether to output as 1 consolidated dataframe or multiple dataframe object. Default is False
    :type combine: Boolean
    '''

    #  Handle Date
    if end_date is None:
        end_date = date.today().isoformat()

    start_date = date_calc(hist)

    # Handle Tickers
    histories = {}
    
    for ticker in tickers:
        print(f"Fetching {ticker}...")
        q = Quote(source="VCI", symbol=ticker)
        # Data Validation
        stock = q.history(start=start_date, end=end_date, interval='1d')
        stock['time'] = pd.to_datetime(stock['time'])
        
        # Add to holder object
        histories[ticker] = stock
        print("Done!\n")

    # Handle Output
    if combine == True:
        return combine_tickers(histories, tickers)
    return histories


def date_calc(range:int):
    '''
    Docstring for date_calc
    
    :param range: Take in today's time and calculate the date diferrence
    :type range: int
    '''
    today = date.today()
    start_date = today - timedelta(days=range)
    return start_date.isoformat()


def combine_tickers(histories, tickers):
    '''
    Docstring for combine_tickers
    
    Helper of fetch_stock(), use to combine tickers into 1 dataset
    '''
    parent = []
    for t in tickers:
        histories[t]['tickers'] = t
        parent.append(histories[t])
    panel = pd.concat(parent, ignore_index=False)
    return panel
