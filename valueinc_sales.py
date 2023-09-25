# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:41:51 2023

@author: luiss
"""

import pandas as pd

data = pd.read_csv('Data/transaction2.csv', sep=';')

#data.info()

# working with calculations

# defining variables
costPerItem = data['CostPerItem']
#sellingPricePerItem = 
numberOfItemsPurchased = data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numberOfItemsPurchased

# adding new columns to dataFrame
data['CostPerTransaction'] = costPerTransaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['Profit'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['Profit'] / data['CostPerTransaction']

# rounding markup

roundMarkup = round(data['Markup'], 2)
data['Markup'] = roundMarkup

# combining data fields
data['Date'] = (data['Day']).astype(str)\
    +'-'+(data['Month']).astype(str)\
    +'-'+(data['Year']).astype(str)
    
data.head()
data.iloc[0:5,-2:]

# using split to split the client keywords field
# and replace to remove unnecessary chars
split_col = data['ClientKeywords'].str.split(',', expand=True)
data['ClientAge'] = split_col[0].str.replace('[','')
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2].str.replace(']','')

# using lower to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# merging files

seasons = pd.read_csv('Data/value_inc_seasons.csv', sep=';')

data = pd.merge(data, seasons, on='Month')

data = data.drop('ClientKeywords', axis=1)
data = data.drop(['Day', 'Month', 'Year'], axis=1)

# EXPORTING INTO CSV
data.to_csv('Data/ValueInc_Cleaned.csv', index=False)



