import tweepy
import pandas as pd
import nltk
import plotly.express as px
import re
from IPython.display import display
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
from PIL import Image


from wordcloud import WordCloud

def plot_sent(key_word,nbTweet):
    tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    nltk.download('vader_lexicon')
    from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    tweet_list = []

    keyword = key_word
    noOfTweet = nbTweet
    tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)

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
    'être',
    'rt',
    'https',
    'de',
    'co']

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

    Number_sentiment= df.groupby(["sentiment"])['text'].count().reset_index().reset_index(drop=True)
    fig = px.histogram(df, x="sentiment",color="sentiment")
    fig.update_layout(
        title_text='Sentiment of reviews', 
        xaxis_title_text='Sentiment', 
        yaxis_title_text='Count', 
        bargap=0.2, 
        bargroupgap=0.1
    )
    fig.write_image(file='static/barplot.jpg', format='jpg')



    fig2 = px.pie(Number_sentiment, values=Number_sentiment['text'], names=Number_sentiment['sentiment'], color_discrete_sequence=px.colors.sequential.Emrld
    )
    fig2.write_image(file='static/piechart.jpg', format='jpg')

    def create_wordcloud(text):
        
        wc = WordCloud(background_color='white',
        max_words=3000,
        stopwords=stop_words,
        repeat=True, width=1800, height=900)
        wc.generate(str(text))
        wc.to_file('static/wc.png')
        print('Word Cloud Saved Successfully')
        path='static/wc.png'
        
        display(Image.open(path))

    create_wordcloud(df['tweet'].values)

