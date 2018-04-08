import os
import tweepy
import json
import twitter_functions

class TwitterUser:

	def __init__(self,username):
		filepath = os.path.join(os.path.dirname(__file__), '../keys.json')
		file = open(filepath)

		keys = json.load(file)
		consumer_key=keys[0]['consumer_key']
		consumer_secret=keys[0]['consumer_secret']
		access_token=keys[0]['access_token']
		access_token_secret=keys[0]['access_token_secret']

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		self.api = tweepy.API(auth)

		user = self.api.get_user(username)

		self.id = user.id
		self.username = user.screen_name
		self.name = user.name
		self.followers_count = user.followers_count
		self.tweets_count = user.statuses_count
		self.following_count = user.friends_count
		self.likes_count = user.favourites_count
		
		file.close()

	def get_last_month_hashtags(self,num_months=1):
		tweets = twitter_functions.get_user_last_months_tweets(self.username, num_months , self.api)
		hashtags = twitter_functions.get_hashtags(tweets)
		return hashtags

