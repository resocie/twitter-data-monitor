import unittest
import datetime
import twitter.twitter_functions as functions
from dateutil.relativedelta import relativedelta

class TestTwitterFunctions(unittest.TestCase):

	def test_time_range(self):
		tweets = functions.get_user_last_month_tweets('jairbolsonaro', num_months=2)

		self.assertEqual(tweets[-1].created_at >= datetime.datetime.now() + relativedelta(months=-2), True)

	def test_hashtags(self):
		api=functions.get_api()
		tweets=api.statuses_lookup([974344829697249282,974338524773265409])
		self.assertEqual(functions.get_hashtags(tweets),['boatardealtamentemaisoumenos', 'filosofage'])	

if __name__ == '__main__':
    unittest.main()