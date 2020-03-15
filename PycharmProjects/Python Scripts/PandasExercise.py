import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/srijan-das/Projects/master/PycharmProjects/Python-for-Finance-Repo-master/03-%20General%20Pandas/Pandas-Exercises/banklist.csv')

#print(df.info())

#print(len(df['ST'].value_counts()))

#print(df['ST'].unique())

#print(df['Acquiring Institution'].value_counts().head(5))

#print(df[df['Acquiring Institution'] == 'State Bank of Texas'])

#print(df[df['ST'] == 'CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1))

#print(sum(df['Bank Name'].apply(lambda name : 'bank' not in name.lower() )))