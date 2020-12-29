import sys
import pandas as pd
import numpy as np
from datetime import date

def validate(ticker):
    if len(ticker) == 0:
        raise IOError("argv cannot be empty")
    return ticker

def extract(fileName):
    return pd.read_csv(fileName)

def correlateStocks(stockDF1, stockDF2):
    openCorrelation = np.correlate(stockDF1['Open'], stockDF2['Open'])
    closeCorrelation = np.correlate(stockDF1['Close'], stockDF2['Close'])
    highCorrelation = np.correlate(stockDF1['High'], stockDF2['High'])
    lowCorrelation = np.correlate(stockDF1['Low'], stockDF2['Low'])
    volumeCorrelation = np.correlate(stockDF1['Volume'], stockDF2['Volume'])

    return pd.DataFrame(np.array([openCorrelation, closeCorrelation, highCorrelation, lowCorrelation, volumeCorrelation]),
                        columns=['Open', 'Close', 'High', 'Low', 'Volume'])
def export(dataFrame, ticker1, ticker2):
    dataFrame.to_csv(path_or_buf="/var/appData/correlation_{0}_{1}_{2}.csv".format(ticker1, ticker2, date.today().strftime("%b-%d-%Y")), index=False)

if __name__ == '__main__':
    ticker1 = validate(sys.argv[1])
    ticker2 = validate(sys.argv[2])

    stock1 = extract("/var/appData/{0}.csv".format(ticker1))
    stock2 = extract("/var/appData/{1}.csv".format(ticker2))

    dataFrame = correlateStocks(stock1, stock2)
    export(ticker1, ticker2, dataFrame)
