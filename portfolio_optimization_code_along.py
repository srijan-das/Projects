import quandl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from alpha_vantage.timeseries import TimeSeries
#import AVdataformatter as tf
#import AVapikeys as rkey
import seaborn as sns

'''
ts = TimeSeries(key=rkey.get_AV_key(), output_format='pandas')

aapl, meta_data = ts.get_daily('AAPL', outputsize='compact')
amzn, meta_data = ts.get_daily('AMZN', outputsize='compact')
cisco, meta_data = ts.get_daily('CSCO', outputsize='compact')
ibm, meta_data = ts.get_daily('IBM', outputsize='compact')

aapl = tf.reformat(aapl)
amzn = tf.reformat(amzn)
cisco = tf.reformat(cisco)
ibm = tf.reformat(ibm)

aapl = aapl[::-1]
amzn = amzn[::-1]
cisco = cisco[::-1]
ibm = ibm[::-1]
'''
aapl = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/AAPL_CLOSE', parse_dates = True)
amzn = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/AMZN_CLOSE', parse_dates = True)
cisco = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/CISCO_CLOSE', parse_dates = True)
ibm = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/09-Python-Finance-Fundamentals/IBM_CLOSE', parse_dates = True)


stocks = pd.concat([aapl['Adj. Close'], amzn['Adj. Close'], cisco['Adj. Close'], ibm['Adj. Close']], axis=1)
stocks.columns = 'AAPL AMZN CSCO IBM'.split()

# Corr of returns
'''
sns.heatmap(stocks.pct_change(1).corr())
plt.show()
print(stocks.pct_change(1).corr())
'''

# best to use log returns instead of regular returns for when detrending is required

log_returns = np.log(stocks / stocks.shift(1))
'''
log_returns.hist(bins=100)
plt.show()
'''

num_ports = 5000
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

# random allocation method

for i in range(0, num_ports) :

    # getting random weights for Monte Carlo sim * weights must add to 1

    weights = np.array(np.random.random(4))
    weights = weights / np.sum(weights)
    all_weights[i,:] = weights
    # Expected Return

    ret_arr[i] = np.sum((log_returns.mean() * weights) * 252)
    
    # Expected Variance ( or Volatility)

    vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*252, weights)))
    # Sharpe Ratio
    RFR = 0
    sharpe_arr[i] = (ret_arr[i] - RFR) / vol_arr[i]

'''    
plt.figure(figsize=(8,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label = 'Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.scatter(vol_arr[sharpe_arr.argmax()], ret_arr[sharpe_arr.argmax()], c='red', edgecolors='black')
plt.show()
'''
#print('With Random allocations : {R} {V} {S} '.format(R=ret_arr[sharpe_arr.argmax()] , V=vol_arr[sharpe_arr.argmax()] , S=sharpe_arr.max()))

# with mathematical optimization

def get_ret_vol_sr(weights) :
    weights = np.array(weights)
    ret = np.sum(log_returns.mean() * weights * 252)
    vol = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*252, weights)))
    sr = ret / vol
    return np.array([ret, vol, sr])

from scipy.optimize import minimize

def neg_sharpe(weights) :
    return get_ret_vol_sr(weights)[2] * -1

def check_sum(weights) :
    return np.sum(weights) - 1

cons = ({'type':'eq', 'fun':check_sum})

bounds = ((0,1),(0,1),(0,1),(0,1))

init_guess = [0.25,0.25,0.25,0.25]

opt_results = minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=cons)

#print('With Mathematical Optimization: ', get_ret_vol_sr(opt_results.x))

frontier_y = np.linspace(0, 0.3, 100)

def minimize_vol(weights) :
    return get_ret_vol_sr(weights)[1]

frontier_vol = []

for possible_return in frontier_y :
    cons = ({'type' : 'eq', 'fun' : check_sum}, {'type' : 'eq', 'fun' : lambda w:get_ret_vol_sr(w)[0]-possible_return})
    result = minimize(minimize_vol, init_guess, method='SLSQP', bounds=bounds, constraints=cons)

    frontier_vol.append(result['fun'])

plt.figure(figsize=(8,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label = 'Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.scatter(vol_arr[sharpe_arr.argmax()], ret_arr[sharpe_arr.argmax()], c='red', edgecolors='black')
plt.plot(frontier_vol, frontier_y, 'g--', linewidth=3)
plt.show()