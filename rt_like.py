import tweepy
import pandas as pd
import re
import json
import pymongo
from pymongo import MongoClient
import seaborn as sns
import matplotlib.pyplot as plt
from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask

def plot_rt():
    plt.style.use('ggplot')

    consumer_key =CONSUMER_KEY
    consumer_secret =CONSUMER_SECRET
    access_token =ACCESS_TOKEN
    access_token_secret  =ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)


    client = MongoClient('localhost', 27017)
    collection=client.election

    list= ['EmmanuelMacron','MLP_officiel','vpecresse','ZemmourEric',
            'JLMelenchon','yjadot','ChTaubira','Anne_Hidalgo','Fabien_Roussel',
            'dupontaignan','f_philippot','jeanlassalle','PhilippePoutou',
            'UPR_Asselineau','n_arthaud','HeleneThouy']

    all_result=[]

    for i in list :
        tweets = api.user_timeline(screen_name=i,count=100,tweet_mode="extended")

        col=collection[i]

        for info in tweets :
            tweet_dict = {
                'candidat': info.user.screen_name,
                'ID': info.id,
                'date': str(info.created_at),
                'rt': info.retweet_count,
                'fav' : info.favorite_count,
                'text' : info.full_text}
            col.insert_one(tweet_dict)

        result=col.aggregate(
            [
                {'$group':
                { 
                    '_id':"$candidat",
                    'avgrt' : { '$avg':'$rt'},
                    'avglike' : { '$avg':'$fav'},
                }
                }
            ]
        )
        for i in result : all_result.append(i)
    df = pd.DataFrame(all_result)
    df = pd.melt(df, id_vars='_id', value_vars=['avgrt', 'avglike'])
    print(df)
    plt.figure(figsize=[16,10])
    g = sns.catplot(
        data=df, kind="bar",
        x="_id", y="value", hue="variable",
        ci="sd", palette="dark", alpha=.6, height=6
    )
    g.despine(left=True)
    g.set_axis_labels("", "total")
    g.legend.set_title("")

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


