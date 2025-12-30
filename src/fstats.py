import pandas as pd
import numpy as np
import scipy as sp
from typing import Iterable


def rolling_zscore(s: pd.Series, window: int):
    mu = s.rolling(window, min_periods=window).mean()
    sd = s.rolling(window, min_periods=window).std(ddof=0)
    return (s-mu)/sd

def summary_stat(p: dict):
    summary_table = {}
    for ticker in p:
        stock_info = p[ticker]
        print(stock_info.describe())
        return 0
        