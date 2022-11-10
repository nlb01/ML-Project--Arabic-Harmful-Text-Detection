import pandas as pd
import csv
import os


neg = 0
zeroes = 0
ones = 0
twos = 0 
threes = 0



with open('Project\\final_data.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    tweets = []
    sentiment = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[2] == '-1':
                neg += 1
            elif row[2] == '0':
                zeroes +=1
            elif row[2] == '1':
                ones += 1
            elif row[2] == '2':
                twos += 1
            else:
                threes += 1


# fn = 'final_data.xlsx' 
# dfs = pd.read_excel(fn, sheet_name='sheet_1')

# sentiments = dfs['class']
# sentiments = sentiments.to_list()

print("negatives = " , neg)
print("zeroes = " , zeroes)
print("ones = " , ones)
print("twos = " , twos)
print("threes = " , threes)