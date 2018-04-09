import os
import tweepy
import json
import twitter_functions

class TwitterUser:

	def __init__(self,username):
		api = twitter_functions.get_api()

		user = api.get_user(username)

		self.id = user.id
		self.username = user.screen_name
		self.name = user.name
		self.followers_count = user.followers_count
		self.tweets_count = user.statuses_count
		self.following_count = user.friends_count
		self.likes_count = user.favourites_count
		

	def get_last_month_hashtags(self,num_months=1):
		api = twitter_functions.get_api()
		tweets = twitter_functions.get_user_last_months_tweets(self.username, num_months)
		hashtags = twitter_functions.get_hashtags(tweets)
		return hashtags

