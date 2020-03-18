from scipy import stats
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

start = pd.to_datetime('2015-01-01')
end = pd.to_datetime('2020-01-01')

spy_etf = web.data.get_data_tiingo('SPY', api_key='f4604e85f25e80abde0747cbdeeecbb7cb5ee3ec', start = start, end = end)

spy_etf = spy_etf.xs('SPY')

# Assuming strategy to be ivesting completely in just apple

aapl = web.data.get_data_tiingo('AAPL', api_key='f4604e85f25e80abde0747cbdeeecbb7cb5ee3ec', start = start, end = end)

aapl = aapl.xs('AAPL')
'''
aapl['close'].plot(label='AAPL')
spy_etf['close'].plot(label='S&P500')
plt.legend()
plt.show()
'''
aapl['Cumulative Returns'] = aapl['close'] / aapl['close'].iloc[0]
spy_etf['Cumulative Returns'] = spy_etf['close'] / spy_etf['close'].iloc[0]

aapl['Daily Return'] = aapl['close'].pct_change(1)
spy_etf['Daily Return'] = spy_etf['close'].pct_change(1)

beta, alpha, r_value, p_value, std_error = stats.linregress(aapl['Daily Returns'].iloc[1:], spy_etf['Daily Returns'].iloc[1:])

# FOR CAPM r(st) = beta*r(mkt) + alpha
# CAPM says aplha is zero, stock returns cannot beat market returns
# Model so alpha not zero, thereby beating the market

