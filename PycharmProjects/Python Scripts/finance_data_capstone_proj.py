import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data, wb
from datetime import datetime
#import os

start = datetime(year= 2012, month=1, day=1)
end = datetime(year= 2017, month=1, day=1)

TSLA_data = data.get_data_tiingo('TSLA', api_key='f4604e85f25e80abde0747cbdeeecbb7cb5ee3ec', start = start, end = end)
Ford_data = data.get_data_tiingo('F', api_key='f4604e85f25e80abde0747cbdeeecbb7cb5ee3ec', start = start, end = end)
GM_data = data.get_data_tiingo('GM', api_key='f4604e85f25e80abde0747cbdeeecbb7cb5ee3ec', start = start, end = end)

#print(TSLA_data)
#print(Ford_data)
#print(GM_data)

TSLA_data = TSLA_data.xs('TSLA')
Ford_data = Ford_data.xs('F')
GM_data = GM_data.xs('GM')

#print(TSLA_data.head(1))
#print(Ford_data.head(1))
#print(GM_data.head(1))

'''
TSLA_data['close'].plot(label='TSLA', title='Close Prices',legend=True)
Ford_data['close'].plot(label='Ford', legend=True)
GM_data['close'].plot(label='GM', legend=True)
plt.show()
'''
'''
TSLA_data['volume'].plot(label='TSLA', title='Volume',legend=True)
Ford_data['volume'].plot(label='Ford', legend=True)
GM_data['volume'].plot(label='GM', legend=True)
plt.show()
'''

#print(Ford_data['volume'].argmax())

TSLA_data['Total Traded'] = TSLA_data['open'] * TSLA_data['volume']
Ford_data['Total Traded'] = Ford_data['open'] * Ford_data['volume']
GM_data['Total Traded'] = GM_data['open'] * GM_data['volume']

'''
TSLA_data['Total Traded'].plot(label='TSLA', title='Total Traded',legend=True)
Ford_data['Total Traded'].plot(label='Ford', legend=True)
GM_data['Total Traded'].plot(label='GM', legend=True)
plt.show()
'''

#print(TSLA_data['Total Traded'].argmax())

TSLA_data['MA50'] = TSLA_data['open'].rolling(50).mean()
TSLA_data['MA200'] = TSLA_data['open'].rolling(200).mean()

Ford_data['MA50'] = Ford_data['open'].rolling(50).mean()
Ford_data['MA200'] = Ford_data['open'].rolling(200).mean()

GM_data['MA50'] = GM_data['open'].rolling(50).mean()
GM_data['MA200'] = GM_data['open'].rolling(200).mean()

'''
TSLA_data['MA50'].plot(label='TSLA', title='MA50',legend=True)
Ford_data['MA50'].plot(label='Ford', legend=True)
GM_data['MA50'].plot(label='GM', legend=True)
plt.show()

TSLA_data['MA200'].plot(label='TSLA', title='MA200',legend=True)
Ford_data['MA200'].plot(label='Ford', legend=True)
GM_data['MA200'].plot(label='GM', legend=True)
plt.show()

TSLA_data['MA50'].plot(label='MA50', title='TSLA',legend=True)
TSLA_data['open'].plot(label='Open', legend=True)
plt.show()
'''

'''
d1 = pd.DataFrame(data=TSLA_data['open'].values, columns=['TSLA Open'])
d2 = pd.DataFrame(data=Ford_data['open'].values, columns=['Ford Open'])
d3 = pd.DataFrame(data=GM_data['open'].values, columns=['GM Open'])

open_df = pd.concat([d1, d2, d3], axis=1)
#open_df.columns = 'TSLA_open Ford_open GM_open'.split()
sns.pairplot(open_df)
plt.show()
'''

TSLA_data['daily returns'] = TSLA_data['close'].pct_change(1)
Ford_data['daily returns'] = Ford_data['close'].pct_change(1)
GM_data['daily returns'] = GM_data['close'].pct_change(1)

'''
sns.distplot(TSLA_data['daily returns'], bins=50, kde=False, label='TSLA Daily Returns')
sns.distplot(Ford_data['daily returns'], bins=50, kde=False, label='Ford Daily Returns')
sns.distplot(GM_data['daily returns'], bins=50, kde=False, label='GM Daily Returns')
plt.legend()
plt.grid()
plt.show()
'''

sns.boxplot(data=TSLA_data, y='daily returns')
sns.boxplot(data=Ford_data, y='daily returns')
sns.boxplot(data=GM_data, y='daily returns')
plt.legend()
plt.show()