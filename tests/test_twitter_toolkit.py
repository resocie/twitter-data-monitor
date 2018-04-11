import unittest
import datetime
from twitter.TwitterToolkit import TwitterAPI
from twitter.TwitterToolkit import TweetTK
from dateutil.relativedelta import relativedelta

class TestTwitterToolkit(unittest.TestCase):

	def test_time_range(self):
		api = TwitterAPI()
		tweets = api.get_user_last_month_tweets('jairbolsonaro', num_months=2)

		self.assertEqual(tweets[-1].created_at >= datetime.datetime.now() + relativedelta(months=-2), True)

	def test_hashtags(self):
		api = TwitterAPI()
		tweets = api.statuses_lookup([974344829697249282,974338524773265409])
		self.assertEqual(TweetTK.extract_hashtags(tweets),['BoaTardeAltamenteMaisOuMenos', 'Filosofage'])		

if __name__ == '__main__':
    unittest.main()