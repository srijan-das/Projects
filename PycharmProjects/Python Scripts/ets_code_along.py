import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv', index_col='Month')

airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
# multiplicative for non linear trends (by eyeballing)
# additive for linear trends
'''
result.seasonal.plot()
plt.show()
result.trend.plot()
plt.show()
result.resid.plot()
plt.show()
'''
'''
result.plot()
plt.show()
'''

