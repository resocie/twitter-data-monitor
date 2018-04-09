import datetime
import os
import json
import tweepy
from dateutil.relativedelta import relativedelta


def get_user_last_month_tweets(username, num_months=1):
    api = get_api()
    tweet_list = []
    min_date = datetime.datetime.now() + relativedelta(months=-num_months)
    temp = api.user_timeline(screen_name=username, count=200, tweet_mode='extended')
    while temp[-1].created_at >= min_date and len(temp)>0:
        tweet_list.extend(temp)
        temp = api.user_timeline(screen_name=username, max_id=(temp[-1].id -1), count=200, tweet_mode='extended')
    for tweet in temp:
        if tweet.created_at >= min_date:
            tweet_list.append(tweet)

    return tweet_list     

def get_hashtags(tweet_list):
    hashtags = []
    for tweet in tweet_list:    
        for hashtag in tweet.entities['hashtags']:
            hashtags.append(hashtag['text'].lower())
    return list(set(hashtags))

def get_api():
    filepath = os.path.join(os.path.dirname(__file__), '../keys.json')
    file = open(filepath)
    keys = json.load(file)
    consumer_key=keys[0]['consumer_key']
    consumer_secret=keys[0]['consumer_secret']
    access_token=keys[0]['access_token']
    access_token_secret=keys[0]['access_token_secret']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    file.close()
    return api

