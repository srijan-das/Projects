import pandas as pd
import quandl
import seaborn as sns

start = pd.to_datetime('2018-03-01')
end = pd.to_datetime('2020-03-10')

quandl.ApiConfig.api_key = "ybjnmxNZ-H-gvZ5U3wvz"

CromptonGreaves = quandl.get('BSE/BOM539876', start_date=start, end_date=end, column_index='4')
TeamLease = quandl.get('BSE/BOM539658', start_date=start, end_date=end, column_index='4')
Ujjivan = quandl.get('BSE/BOM539874', start_date=start, end_date=end, column_index='4')

principal = 100000 # amount invested

for stock_df in (CromptonGreaves,TeamLease, Ujjivan) :
    stock_df['Norm Returns'] = stock_df['Close'] / stock_df.iloc[0]['Close']

# 30% in Cromp, 40% in Ujj, 30% in TL

for stock_df , allo in zip((CromptonGreaves,TeamLease, Ujjivan),(0.3,0.4,0.3)) :
    stock_df['Allocated'] = stock_df['Norm Returns'] * allo

for stock_df in [CromptonGreaves,TeamLease, Ujjivan] :
    stock_df['Position Values'] = stock_df['Allocated'] * principal

portfolio_val = pd.concat([CromptonGreaves['Position Values'], TeamLease['Position Values'], Ujjivan['Position Values']], axis=1)
portfolio_val.columns = ['CG Pos', 'TL Pos', 'UJJ Pos']

portfolio_val['Total Pos'] = portfolio_val.sum(axis=1)

import matplotlib.pyplot as plt
'''
portfolio_val.plot()
plt.show()
'''

portfolio_val['Daily Returns'] = portfolio_val['Total Pos'].pct_change(1)

'''
portfolio_val['Daily Returns'].plot(kind='kde')
plt.show()
'''

# Calculating Sharpe Ratio

RFR = 0 # Risk free return rate

SR = (portfolio_val['Daily Returns'].mean() - RFR) / portfolio_val['Daily Returns'].std()

'''
Annualized Sharpe ratio
--> Multiply SR with k = sqrt(252) for daily sampling rate
--> Multiply SR with k = sqrt(36) for weekly sampling rate
--> Multiply SR with k = 1 for yearly sampling rate
'''

ASR = SR * (252**0.5)

