import unittest
import os
import json
import tweepy
import datetime
import twitter.twitter_functions as twitter_functions
from dateutil.relativedelta import relativedelta

class TestTwitterFunctions(unittest.TestCase):

	def test_time_range(self):
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
		tweets = twitter_functions.get_user_last_months_tweets('jairbolsonaro', 2, api)

		self.assertEqual(tweets[-1].created_at >= datetime.datetime.now() + relativedelta(months=-2), True)


if __name__ == '__main__':
    unittest.main()