import csv
import datetime
import os
import json
import tweepy
from dateutil.relativedelta import relativedelta

class TwitterAPI(tweepy.API):

    def __init__(self,keys="../keys.json"):
        filepath = os.path.join(os.path.dirname(__file__), keys)
        file = open(filepath)
        keys = json.load(file)
        consumer_key=keys[0]['consumer_key']
        consumer_secret=keys[0]['consumer_secret']
        access_token=keys[0]['access_token']
        access_token_secret=keys[0]['access_token_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        tweepy.API.__init__(self,auth)
        file.close()


    def get_user_last_month_tweets(self,username, num_months=1):
        tweet_list = []
        min_date = datetime.datetime.now() + relativedelta(months=-num_months)
        temp = self.user_timeline(screen_name=username, count=200, tweet_mode='extended')
        while temp[-1].created_at >= min_date and len(temp)>0:
            tweet_list.extend(temp)
            temp = self.user_timeline(screen_name=username, max_id=(temp[-1].id -1), count=200, tweet_mode='extended')
        for tweet in temp:
            if tweet.created_at >= min_date:
                tweet_list.append(tweet)

        return tweet_list

    def criar_csv():
        with open('twitter/autores.csv', 'w') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow(["nome", "seguidores", "tweets", "seguindo", "curtidas"])
            csvfile.close()

    def atualizar_csv_novos_autores(self):
        with open('twitter/autores.csv', 'a') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow([self.name, self.followers_count,
            self.tweets_count, self.following_count, self.likes_count])
            csvfile.close()


class TweetTK:

    @staticmethod
    def extract_hashtags(tweet_list):
        hashtags = []
        for tweet in tweet_list:
            for hashtag in tweet.entities['hashtags']:
                hashtags.append(hashtag['text'])
        return list(set(hashtags))
