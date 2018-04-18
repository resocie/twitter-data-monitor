import unittest
import warnings
import datetime
from twitter.TwitterToolkit import TwitterAPI, TweetTK
from dateutil.relativedelta import relativedelta

class TestTwitterToolkit(unittest.TestCase):

	# time consuming
	def test_time_range(self):
		warnings.filterwarnings("ignore", category=ResourceWarning)
		api = TwitterAPI()
		tweets = api.get_user_last_month_tweets('jairbolsonaro', num_months=2)
		tweets2 = api.get_user_tweets_from('cirogomes', day=2, month=4, year=2018) 
		self.assertEqual(tweets[-1].created_at >= datetime.datetime.now() + relativedelta(months=-2), True)
		self.assertEqual(tweets2[-1].created_at >= datetime.datetime(2018, 4, 2), True)


	def test_hashtags(self):
		api = TwitterAPI()
		tweets = api.statuses_lookup([974344829697249282,974338524773265409])
		self.assertIn("Filosofage",TweetTK.extract_hashtags(tweets))
		self.assertIn("BoaTardeAltamenteMaisOuMenos",TweetTK.extract_hashtags(tweets))
if __name__ == '__main__':
    unittest.main()
     