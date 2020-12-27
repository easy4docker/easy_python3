import pandas as pd
import yfinance as yf

from datetime import date

def fetchWatchlist(fileName):
    dataFrame = pd.read_csv(fileName)
    return dataFrame["Symbol"].tolist()

def fetchTicker(tickers, period="10y"):
    yTickers = yf.Tickers(" ".join(tickers))
    dataFrame = pd.DataFrame()
    for tindex in range(len(tickers)):
        history = yTickers.tickers[tindex].history(period=period)
        filtered = history.filter(items=['Open', 'Close', 'High', 'Low', 'Volume'])
        filtered.reset_index(inplace=True, col_level=0)
        filtered.insert(0, "Ticker", yTickers.tickers[tindex].ticker, True)

        dataFrame = pd.concat([dataFrame, filtered])
    return dataFrame

def batchedFetchTicker(fetchList):
    dataFrame = pd.DataFrame()
    total = len(fetchList)
    fromFetched = 0
    while fromFetched < total:
        toFetched = total if total - fromFetched < 254 else fromFetched + 254
        toExport = fetchTicker(fetchList[fromFetched:toFetched])
        dataFrame = pd.concat([dataFrame, toExport])
        fromFetched = toFetched + 1
    return dataFrame


def export(dataFrame):
    dataFrame.to_csv(path_or_buf="/var/appData/{0}.csv".format(date.today().strftime("%b-%d-%Y")), index=False)

# to run type 'sh setup.sh'
if __name__ == '__main__':
    watchList = fetchWatchlist("/var/inputs/500.csv")
    dataFrame = batchedFetchTicker(watchList)
    export(dataFrame)
