# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:35:13 2023

@author: luiss
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json data
json_file = open('Data/loan_data_json.json')
data = json.load(json_file)

# method 2 to read json data
with open('Data/loan_data_json.json') as json_file:
    data = json.load(json_file)

#transforam to dataframe
loandata = pd.DataFrame(data)

# finding unique values for the purpose column
loandata['purpose'].unique()

# describe the data
loandata.describe()

# describe the data of a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

ficocat = []
for i in range(0,len(loandata)):
    category = loandata['fico'][i]

    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 660:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)

loandata['fico.category'] = pd.Series(ficocat)

# for interest rates, a bnew column is wanted. rate >0.12 then high, else low
loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# number of loan/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green', width=0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red',width=0.1)
plt.show()

# scatter plots
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color='#4caf50')
plt.show()


# writing to csv
loandata.to_csv('Data/loan_cleaned.csv', index=True)

































