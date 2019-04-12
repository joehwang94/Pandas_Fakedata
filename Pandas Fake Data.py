#Please install pandas onto your drive if you haven't done so already. This will not run without it.
#To install it, type in "pip install pandas" (without the quotes) in your command prompt before running this script.


import pandas as pd


df = pd.read_csv('fakedata.csv', index_col = 0)


print(df)

print('Minimum Revenue: ', df['Revenue'].min())
print('Maximum Revenue: ', df['Revenue'].max())
print('Total Customers: ', df['Customers'].sum())
print('Median Number of Customers: ', df['Customers'].median())
print('Average Number of Customers: ', df['Customers'].mean())
print('Number of Cities: ', df['City'].count())
print('Minimum Average City Volume: ', df['AvgVolume'].min())
