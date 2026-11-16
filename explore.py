print("---Exercise 1---")

import pandas as pd 
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("---Exercise 2---")

south = df[df['region'] == 'South'] #mask; it will filter out other regions, only returning south region data
print(len(south))
print(south.head())

print("---Exercise 3---")

print(df.sort_values('revenue', ascending=False).head(5))
