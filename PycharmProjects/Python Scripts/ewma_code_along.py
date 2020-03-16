import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/08-Time-Series-Analysis/airline_passengers.csv', index_col='Month')

airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

airline['6 M SMA'] = airline['Thousands of Passengers'].rolling(6).mean()

'''
airline[['6 M SMA', 'Thousands of Passengers']].plot()
plt.show()
'''

airline['12 M SMA'] = airline['Thousands of Passengers'].rolling(12).mean()

'''
airline.plot()
plt.show()
'''

airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()

airline[['12 M SMA','EWMA-12','Thousands of Passengers']].plot()
plt.show()