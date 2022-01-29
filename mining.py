import tweepy
import pandas as pd
from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

cursor = tweepy.Cursor(api.user_timeline, id='EmmanuelMacron', tweet_mode="extended").items(5)

for i in cursor:
    print(i)