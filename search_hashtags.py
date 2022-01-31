import tweepy
import pandas as pd

def hashtags_df(word,nofTwit):
        from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret



        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        words= word


        db = pd.DataFrame(columns=['username','description',
                                'location','following',
                                'followers','totaltweets',
                                'retweetcount','text','hashtags'])


        tweets = tweepy.Cursor(api.search_tweets,
                                q='{words}-filter:retweets'.format(words=words),
                                tweet_mode='extended').items(nofTwit)

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
        return db.sort_values(by=['retweetcount'], ascending=False).head(nofTwit)