import csv
import re
import pandas as pd
import openpyxl

data = []

with open('test_arabic_1.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    tweets = []
    sentiment = []
    for row in csv_reader:
        if line_count <= 1:
            line_count += 1
        else:
            line_count += 1

            tweet = row[0]
            sent = row[1]

            if sent == "normal":
                sent = 0
            elif sent == "abusive":
                sent = 2
            elif sent == "hate":
                sent = 1
            
            row = [tweet, sent]
            data.append(row)
            

df = pd.DataFrame(data, columns=['Tweets', 'class'])

df.to_excel('test_arabic_1_adjust.xlsx', sheet_name='sheet_1' , encoding='utf-8')
