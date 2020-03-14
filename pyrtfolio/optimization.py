import investpy
import pandas as pd

stocks = ['AAPL', 'NFLX']

data = pd.DataFrame(columns=stocks)

for stock in stocks:
    data[stock] = investpy.get_stock_historical_data(stock=stock, country='united states', from_date='01/01/2019', to_date='31/12/2019')['Close'].tolist()

print(data)

from pprint import pprint
import numpy as np

data = (data / data.shift(1)) * 100 - 100

data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

pprint(data)

for stock in stocks:
    pprint(np.var(np.asarray(data[stock])))
    pprint(np.var(np.asarray(data[stock]))**2)

pprint(np.corrcoef(x=data['AAPL'], y=data['NFLX']))