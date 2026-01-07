from vnstock import Quote
from datetime import date, timedelta
from typing import Iterable, Optional
import pandas as pd
import numpy as np
from time import sleep

'''
FETCH_INFO
    This library is use to fetch and validate info from the vnstock library

'''

def fetch_stock(tickers: Iterable[str], interval: str, hist: int, end_date: Optional[str] = None, combine: Optional[bool] = False):
    '''
    Docstring for fetch_stock
    Use to grab an array of tickers from the Vietnamese stock market via the vnstock library, ensure consistency in timeframe. Can output to a single dataframe for correlation analysis

    :param tickers: Takes in an array of tickers, as string
    :type tickers: Iterable[str]
    :param interval: Takes in a string followed vnstock Quote object ('1m', '5m', '1d', ...)
    :type interval: str
    :param hist: No. of historical date
    :type hist: int
    :param end_date: The end date of the observations
    :type end_date: Optional[str]
    :param combine: Combine to a single dataframe with tickers, else will output as an array of individual ticker dataframe
    :type combine: Optional[bool]
    '''

    #  Handle Date
    if end_date is None:
        end_date = date.today().isoformat()

    start_date = date_calc(hist)

    # Handle Tickers
    histories = {}

    
    df = []
    # Split the API call into smaller chunk calls:
    if len(tickers) > 30:
        df = np.array_split(tickers, len(tickers) % 30)
        sleep_val = 10
    else:
        df = np.array_split(tickers, 2)
        sleep_val = 1

    for batch in df:
        print(f"Processing batch {batch}")
        sleep(sleep_val)
        for ticker in batch:
            q = Quote(source="VCI", symbol=ticker)
            # Data Validation
            stock = q.history(start=start_date, end=end_date, interval=interval)
            stock['time'] = pd.to_datetime(stock['time'])
            
            # Add to holder object
            histories[ticker] = stock
        print("Done!\n")

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
