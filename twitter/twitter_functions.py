import datetime
from dateutil.relativedelta import relativedelta


def get_user_last_months_tweets(username, num_months, api):
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
            hashtags.append(hashtag['text'])
    return list(set(hashtags))

