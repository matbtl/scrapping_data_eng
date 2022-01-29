from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import plotly.express as px
import re
import string
import textblob_fr
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())

#from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

consumer_key ="O3tWUg2VwSo1YEeGYzNtd3fZw"
consumer_secret ="aN1WgHgaIFxxNI9dULaO59gVVBhngoAP6lSn0oLTwWjNxMlyXi"
access_token ="1486708069102936065-8bToI65WDWwErxQIlbTznyTuCSe96p"
access_token_secret  ="roRW8CgJObee3WkQpPYiFdgZBgBmslsXxqZMD8tpu34TC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweet_list = []

#keyword = input('Please enter keyword or hashtag to search: ')
#noOfTweet = int(input ('Please enter how many tweets to analyze: '))
tweets = tweepy.Cursor(api.search_tweets, q='#Macron2022').items(30)

for tweet in tweets:
    tweet_list.append(tweet.text)

df = pd.DataFrame(tweet_list)
df.columns = ['text']


df['text']= df['text'].str.lower()

clean_text=[]
for comment in df['text'].apply(str):
    Word_Tok = []
    for word in  re.sub("\W"," ",comment ).split():
        Word_Tok.append(word)
    clean_text.append(Word_Tok)

df["Word_Tok"]= clean_text


stop_words=[
'alors',
'au',
'aucuns',
'aussi',
'autre',
'avant',
'avec',
'avoir',
'bon',
'car',
'ce',
'cela',
'ces',
'ceux',
'chaque',
'ci',
'comme',
'comment',
'dans',
'des',
'du',
'dedans',
'dehors',
'depuis',
'devrait',
'doit',
'donc',
'dos',
'début',
'elle',
'elles',
'en',
'encore',
'essai',
'est',
'et',
'eu',
'fait',
'faites',
'fois',
'font',
'hors',
'ici',
'il',
'ils',
'je',	
'juste',
'la',
'le',
'les',
'leur',
'là',
'ma',
'maintenant',
'mais',
'mes',
'mien',
'moins',
'mon',
'mot',
'même',
'ni',
'nommés',
'notre',
'nous',
'ou',
'où',
'par',
'parce',
'pas',
'peut',
'peu',
'plupart',
'pour',
'pourquoi',
'quand',
'que',
'quel',
'quelle',
'quelles',
'quels',
'qui',
'sa',
'sans',
'ses',
'seulement',
'si',
'sien',
'son',
'sont',
'sous',
'soyez',
'sujet',
'sur',
'ta',
'tandis',
'tellement',
'tels',
'tes',
'ton',
'tous',
'tout',
'trop',
'très',
'tu',
'voient',
'vont',
'votre',
'vous',
'vu',
'ça',
'étaient',
'état',
'étions',
'été',
'être']

deselect_stop_words = ['n\'', 'ne','pas','plus','personne','aucun','ni','aucune','rien']
for w in deselect_stop_words:
    if w in stop_words:
        stop_words.remove(w)
    else:
        continue


result=[]
for comment in df["Word_Tok"]:
    resultlist = [w for w in comment if not ((w in stop_words) or (len(w) == 1))]
    result.append(' '.join(resultlist))

df["tweet"]=result
print(df.head())

senti_list = []
for i in df["tweet"]:
    vs = tb(i).sentiment[0]
    if (vs > 0):
        senti_list.append('Positive')
    elif (vs < 0):
        senti_list.append('Negative')
    else:
        senti_list.append('Neutral') 

df["sentiment"]=senti_list
print(df)

#plot
Number_sentiment= df.groupby(["sentiment"])['text'].count().reset_index().reset_index(drop=True)
fig = px.histogram(df, x="sentiment",color="sentiment")
fig.update_layout(
    title_text='Sentiment of reviews', # title of plot
    xaxis_title_text='Sentiment', # xaxis label
    yaxis_title_text='Count', # yaxis label
    bargap=0.2, 
    bargroupgap=0.1
)
fig.show()

# fig2 = px.pie(Number_sentiment, values=Number_sentiment['text'], names=Number_sentiment['sentiment'], color_discrete_sequence=px.colors.sequential.Emrld
# )
# fig2.show()



