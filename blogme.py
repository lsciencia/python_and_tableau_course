# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:35:17 2023

@author: luiss
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# reading excel (xlsx) files
data = pd.read_excel('Data/articles.xlsx')

# summary of the data
data.describe()

# summiary of the columns
data.info()

# counting the number of articles per source
# format of groupby: df.groupby(['column_to_group'])['column_to_count'].count()
data.groupby(['source_id'])['article_id'].count()

# num of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping a column
data = data.drop('engagement_comment_plugin_count', axis=1)



# creating a keyword flag
# keyword = 'crash'

# # lets create a for loop to isolate each title row
# keyword_flag = []
# for i in range(0, len(data)):
#     heading = str(data['title'][i])
#     if keyword in heading:
#         flag = 1
# ##    else:
# #        flag = 0
# #    keyword_flag.append(flag)

#data['keyword_flag'] = pd.Series(keyword_flag)

def keywordFlag(keyword):
    # lets create a for loop to isolate each title row
    keyword_flag = []
    
    for i in range(0, len(data)):
        heading = data['title'][i]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
        
    return keyword_flag

keywordflag = keywordFlag('murder')
data['keyword_flag'] = pd.Series(keywordflag)

#sentiment intensity analyzer
sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

sent_int = SentimentIntensityAnalyzer()
for i in range(0, len(data)):
    try:
        sent = sent_int.polarity_scores(data['title'][i])    
        title_neg_sentiment.append(sent['neg'])
        title_pos_sentiment.append(sent['pos'])
        title_neu_sentiment.append(sent['neu'])
    except:
        title_neg_sentiment.append(0)
        title_pos_sentiment.append(0)
        title_neu_sentiment.append(0)
        
data['title_neg_sentiment'] = pd.Series(title_neg_sentiment)
data['title_pos_sentiment'] = pd.Series(title_pos_sentiment)
data['title_neu_sentiment'] = pd.Series(title_neu_sentiment)

data.to_excel('Data/blogme_clean.xlsx', sheet_name='blogmedata', index=False)



















