import csv
import re
import pandas as pd
import openpyxl

data = []

fn = 'retrieved.xlsx' 
dfs1 = pd.read_excel(fn, sheet_name='sheet_1')

Tweets1 = dfs1['Tweets']
Tweets1 = Tweets1.to_list()

sentiments1 = dfs1['Class']
sentiments1 = sentiments1.to_list()

i = 0
for tweet in Tweets1:
        tweet = re.sub('@[a-zA-Z1-9]*' , '', tweet)
        tweet = re.sub('[a-zA-Z]*' , '', tweet)

        for ch in tweet:
            if ('\u0600' <= ch <= '\u06FF' or
                '\u0750' <= ch <= '\u077F' or
                '\u08A0' <= ch <= '\u08FF' or
                '\uFB50' <= ch <= '\uFDFF' or
                '\uFE70' <= ch <= '\uFEFF' or
                '\U00010E60' <= ch <= '\U00010E7F' or
                '\U0001EE00' <= ch <= '\U0001EEFF'):

                data.append([tweet , sentiments1[i]])
                break
        i += 1

df = pd.DataFrame(data, columns=['Tweets', 'class'])

df.to_excel('retrieved_adjust.xlsx', sheet_name='sheet_1' , encoding='utf-8')
