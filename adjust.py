import csv
import re
import pandas as pd
import openpyxl


with open('arabic_dataset_mlma.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    tweets = []
    sentiment = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            sentiment.append(row[2])

            tweet = row[1]
            sent = row[2]

            tweet = re.sub('@[a-z A-Z 1-9]*' , ' ', tweet)
            tweets.append(tweet)


normal = ["normal"]

hateful = ["hateful_normal" , "hateful" , "abusive_hateful" 
,"offensive_hateful" ,"abusive_offensive_hateful_disrespectful_normal" 
, "fearful_disrespectful_hateful_normal" , "abusive_offensive_disrespectful_hateful_normal"
 ,"fearful_abusive_disrespectful_hateful_normal", "hateful_disrespectful" 
 ,"abusive_offensive_hateful_disrespectful" , "fearful_abusive_hateful_disrespectful_normal"
 ,"fearful_offensive_hateful_normal" , "hateful_disrespectful_normal" ,
 "fearful_abusive_offensive_hateful_normal" ,]

abusive = ["abusive_disrespectful" , "abusive" , 
"abusive_offensive" , "abusive_normal" ,"abusive_offensive_hateful_normal" 
, "abusive_disrespectful_hateful_normal" , "fearful_abusive_offensive_hateful"]

disr_off_bullying = ["offensive" , "offensive_disrespectful" ,
 "offensive_normal", "disrespectful" ,"disrespectful_normal" 
 , "fearful_abusive_offensive_hateful_disrespectful" ,
 "fearful_abusive_offensive_disrespectful_normal" ,"fearful_offensive_disrespectful_hateful_normal",
  "abusive_offensive_disrespectful_normal" , "fearful_disrespectful" , 
  "offensive_hateful_disrespectful_normal" , "disrespectful_hateful" , "fearful_offensive_hateful_disrespectful_normal"]

other = ["fearful" ,"fearful_normal" , ]

data = []

i = 0
sent_class = []
for sent in sentiment:
    row = [tweets[i]]
    i += 1
    if sent in normal:
        row.append(0)
    elif sent in hateful:
        row.append(1)
    elif sent in abusive:
        row.append(2)
    elif sent in disr_off_bullying:
        row.append(3)
    elif sent in other:
        row.append(-1)
    data.append(row)


df = pd.DataFrame(data, columns=['Tweets', 'class'])

df.to_excel('adjusted_tweets_mlma.xlsx', sheet_name='sheet_1' , encoding='utf-8')
