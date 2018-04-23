import unittest
import warnings
import datetime
import modules
from modules.twitter_api import TwitterAPI
from dateutil.relativedelta import relativedelta

class TestTwitterAPI(unittest.TestCase):

	# time consuming
	def test_time_range(self):
		warnings.filterwarnings("ignore", category=ResourceWarning)
		api = TwitterAPI()
		tweets2 = api.get_user_tweets_from('cirogomes', day=2, month=4, year=2018)
		self.assertEqual(tweets2[-1].created_at >= datetime.datetime(2018, 4, 2), True)


	def test_hashtags(self):
		api = TwitterAPI()
		tweets = api.statuses_lookup([974344829697249282,974338524773265409])
		self.assertIn("Filosofage",TwitterAPI.extract_hashtags(tweets))
		self.assertIn("BoaTardeAltamenteMaisOuMenos",TwitterAPI.extract_hashtags(tweets))

if __name__ == '__main__':
    unittest.main()
