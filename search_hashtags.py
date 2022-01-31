import tweepy
import pandas as pd
import re

def hashtags(word,nofTwit):
        consumer_key ="O3tWUg2VwSo1YEeGYzNtd3fZw"
        consumer_secret ="aN1WgHgaIFxxNI9dULaO59gVVBhngoAP6lSn0oLTwWjNxMlyXi"
        access_token ="1486708069102936065-8bToI65WDWwErxQIlbTznyTuCSe96p"
        access_token_secret  ="roRW8CgJObee3WkQpPYiFdgZBgBmslsXxqZMD8tpu34TC"


        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        words= word


        # def printtweetdata(n, final_db):
        #         print()
        #         print(f"Tweet {n}:")
        #         print(f"Username:{final_db[0]}")
        #         print(f"Description:{final_db[1]}")
        #         print(f"Location:{final_db[2]}")
        #         print(f"Following Count:{final_db[3]}")
        #         print(f"Follower Count:{final_db[4]}")
        #         print(f"Total Tweets:{final_db[5]}")
        #         print(f"Retweet Count:{final_db[6]}")
        #         print(f"Tweet Text:{final_db[7]}")
        #         print(f"Hashtags Used:{final_db[8]}")


        db = pd.DataFrame(columns=['username','description',
                                'location','following',
                                'followers','totaltweets',
                                'retweetcount','text','hashtags'])


        tweets = tweepy.Cursor(api.search_tweets,
                                words,
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
                        
        return db.sort_values(by=['retweetcount'], ascending=False).head(10)

db = hashtags('Macron2022',30)



print(db)
# for i in final_db.iterrows():
#         print('-----------------------------------------------------------')
#         print(i)
#         print('-----------------------------------------------------------')






        


