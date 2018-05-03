import pytest
import warnings
import datetime
import modules
import pickle
from modules.twitter_api import TwitterAPI
from dateutil.relativedelta import relativedelta

class TestTwitterAPI(unittest.TestCase):
	# time consuming
	def test_time_range():
		warnings.filterwarnings("ignore", category=ResourceWarning)
		api = TwitterAPI()
		tweets2 = api.get_user_tweets_from('cirogomes', day=2, month=4, year=2018)
		assert(tweets2[-1].created_at >= datetime.datetime(2018, 4, 2)) == True

	def test_hashtags():
		warnings.filterwarnings("ignore", category=ResourceWarning)
		tweets = pickle.load(open('tests/tweetlist.p', 'rb'))
		hashtags = TwitterAPI.extract_hashtags(tweets)
		assert 'MaioMesDaCiencia' in hashtags
		assert 'ResolviEsperar' in hashtags
		assert 'Codaí' in hashtags

	def test_mentions():
		warnings.filterwarnings("ignore", category=ResourceWarning)
		tweets = pickle.load(open('tests/tweetlist.p', 'rb'))
		mentions = TwitterAPI.extract_mentions(tweets)
		assert 'davirsimoes' in mentions
		assert 'sonolencio' in mentions
		assert 'Pirulla25' in mentions

if __name__ == '__main__':
    unittest.main()
