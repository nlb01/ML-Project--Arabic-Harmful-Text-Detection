
from fileinput import filename
import pandas as pd

fn = 'data.xlsx' 
dfs = pd.read_excel(fn, sheet_name='sheet_1')

Tweets = dfs['Tweets']
Tweets = Tweets.to_list()

sentiments = dfs['class']
sentiments = sentiments.to_list()

fn = 'retrieved_adjust.xlsx' 
dfs1 = pd.read_excel(fn, sheet_name='sheet_1')

Tweets1 = dfs1['Tweets']
Tweets1 = Tweets1.to_list()

sentiments1 = dfs1['class']
sentiments1 = sentiments1.to_list()

data = []

i = 0
for tweet in Tweets:
    row = [tweet , sentiments[i]]
    i += 1
    data.append(row)

i = 0
for tweet in Tweets1:
    row = [tweet , sentiments1[i]]
    i += 1
    data.append(row)


df = pd.DataFrame(data, columns=['Tweets', 'class'])

df.to_excel('final_data.xlsx', sheet_name='sheet_1' , encoding='utf-8')

