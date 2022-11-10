from numpy import append
import tweepy
import configparser
import csv
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open('GHDS.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    ids = []
    classes = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            line_count += 1
            ids.append(row[1])
            classes.append(row[2])

data = []
unauthorized = 0
i = 0
for id in ids:
    try:
        tweet = api.get_status(str(id))
        print("here-----2")
        data.append([tweet.text , classes[i]])
    except:
        unauthorized += 1
    i += 1

df = pd.DataFrame(data, columns=['Tweets', 'Class'])

df.to_excel('retrieved.xlsx', sheet_name='sheet_1' , encoding='utf-8')


