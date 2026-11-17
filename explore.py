print("---Exercise 1---")

import pandas as pd 
df = pd.read_csv('data/retail_sales.csv')
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

print("=" * 30) #Spacer
print("---Exercise 2---")

south = df[df['region'] == 'South'] #mask; it will filter out other regions, only returning south region data
print(len(south))
print(south.head())
print("=" * 30) #Spacer
print("---Exercise 3---")

print(df.sort_values('revenue', ascending=False).head(5))
print("=" * 30) #Spacer
print("---Exercise 4---")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head(5))

print("=" * 30) #Spacer
print("---Exercise 5---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print("=" * 30) #Spacer
print("---Exercise 6---")
#Method 1 - unique tells us IF we operate in a region
print(df['region'].unique())

#Method 2 - value_counts tells us HOW MUCH business we do there
print(df['region'].value_counts())

print("=" * 30) #Spacer
print("---Exercise 7---")

df_subset = df[['region', 'product', 'revenue']]
print(df_subset.shape)
print("=" * 30) #Spacer
print("---Exercise 8---")

df.to_csv('data/explored.csv', index=False)

#Reflection Questions:
#1. Without looking at your code, can you explain what a boolean filter does in plain English?
# A boolean filter is a way to select rows from a DataFrame based on a condition. It returns a new DataFrame containing only the rows where the condition is True.
#2. What is the difference between df["revenue"] and df[["revenue"]]? When does the distinction matter?
# df["revenue"] returns a Series (1D array) of the revenue column, while df[["revenue"]] returns a DataFrame (2D array) with one column. The distinction matters when you want to maintain the DataFrame structure for further operations or when you need to pass a DataFrame to functions that expect a 2D input.
#3.  If a colleague who only knows Excel asked you to explain why you would choose pandas for this task, what is the single most compelling reason you would give?
# The most compelling reason to choose pandas over Excel is its ability to handle large datasets efficiently and perform complex data manipulations and analyses programmatically, which can save time and reduce errors compared to manual operations in Excel.