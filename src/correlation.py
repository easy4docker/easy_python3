import sys
import pandas as pd
import numpy as np

from datetime import date
from os import path

def validate(ticker):
    if not path.isfile("/var/appData/{0}.csv".format(ticker)):
        raise IndexError(ticker + " ticker is not indexed")
    return ticker

def extract(fileName):
    return pd.read_csv(fileName)

def correlateStocks(stockDF1, stockDF2):
    data = dict()
    data['Open'] = np.correlate(stockDF1['Open'], stockDF2['Open'])
    data['Close'] = np.correlate(stockDF1['Close'], stockDF2['Close'])
    data['High'] = np.correlate(stockDF1['High'], stockDF2['High'])
    data['Low'] = np.correlate(stockDF1['Low'], stockDF2['Low'])
    data['Volume'] = np.correlate(stockDF1['Volume'], stockDF2['Volume'])

    return pd.DataFrame(data)

def export(dataFrame, ticker1, ticker2):
    dataFrame.to_csv(path_or_buf="/var/appData/correlation_{0}_{1}_{2}.csv".format(ticker1, ticker2, date.today().strftime("%b-%d-%Y")), index=False)

if __name__ == '__main__':
    ticker1 = validate(sys.argv[1])
    ticker2 = validate(sys.argv[2])

    stock1 = extract("/var/appData/{0}.csv".format(ticker1))
    stock2 = extract("/var/appData/{0}.csv".format(ticker2))

    dataFrame = correlateStocks(stock1, stock2)
    export(dataFrame, ticker1, ticker2)
