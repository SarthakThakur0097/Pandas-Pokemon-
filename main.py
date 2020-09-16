import pandas as pd

df = pd.read_csv('pokemon_data.csv')

## Read Headers (column names)
print(df.columns)

## Read each Column
print(df['Name'][0:5]) ##Top 5 names

## Read multiple columns
print(df[['Name', 'Type 1', 'HP']])

## Read each Row
print(df.iloc[1])

## Read multiple Rows
print(df.iloc[0:4])

## Read a specific Loaction (R, C)
print(df.iloc[2,1])

## Read each Row
for index, row in df.iterrows():
    print(index, row['Name'])
    
df.loc[df['Type 1'] == 'Fire']