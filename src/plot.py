import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def close_price(df: pd.DataFrame):
    plt.plot(df['time'], df['close'])
    plt.xaxis.set_major_formatter(date_format)
