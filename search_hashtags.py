import tweepy
import pandas as pd
import re


consumer_key ="O3tWUg2VwSo1YEeGYzNtd3fZw"
consumer_secret ="aN1WgHgaIFxxNI9dULaO59gVVBhngoAP6lSn0oLTwWjNxMlyXi"
access_token ="1486708069102936065-8bToI65WDWwErxQIlbTznyTuCSe96p"
access_token_secret  ="roRW8CgJObee3WkQpPYiFdgZBgBmslsXxqZMD8tpu34TC"
 
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

words= "#pecresse2022"


def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Description:{ith_tweet[1]}")
        print(f"Location:{ith_tweet[2]}")
        print(f"Following Count:{ith_tweet[3]}")
        print(f"Follower Count:{ith_tweet[4]}")
        print(f"Total Tweets:{ith_tweet[5]}")
        print(f"Retweet Count:{ith_tweet[6]}")
        print(f"Tweet Text:{ith_tweet[7]}")
        print(f"Hashtags Used:{ith_tweet[8]}")


db = pd.DataFrame(columns=['username','description',
                           'location','following',
                            'followers','totaltweets',
                            'retweetcount','text','hashtags'])
 

tweets = tweepy.Cursor(api.search_tweets,
                               words,
                               tweet_mode='extended').items(15)

list_tweets = [tweet for tweet in tweets]
i=1
for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                location = tweet.user.location
                following = tweet.user.friends_count
                followers = tweet.user.followers_count
                totaltweets = tweet.user.statuses_count
                retweetcount = tweet.retweet_count
                hashtags = tweet.entities['hashtags']

                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                hashtext = list()
                for j in range(0, len(hashtags)):
                        hashtext.append(hashtags[j]['text'])
 

                ith_tweet = [username, description,
                            location, following,
                            followers, totaltweets,
                            retweetcount, text, hashtext]

                db.loc[len(db)] = ith_tweet
                #printtweetdata(i, ith_tweet)
                i = i+1


def clean_tweet(self, tweets):
    tweets = re.sub(r'@[A-Za-z0-9]+','',tweets) #supprime les mentions
    tweets = re.sub(r'#','', tweets) # Supprime le symbole '#'
    tweets = re.sub(r'RT[\s]+', '', tweets) # supprime "RT"
    tweets = re.sub(r'https?:\/\/\S+' ,'', tweets) #supprime les liens 

    return tweets

print(db)