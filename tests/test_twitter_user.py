import pytest
import warnings
from modules.twitter_user import TwitterUser
from modules.twitter_api import TwitterAPI

class TestTwitterUser(unittest.TestCase):

        def test_name_retrieval():
                user = TwitterUser('siqueiralex')
                assert user.name == 'Alex Siqueira'

	def test_id_retrieval():
		user = TwitterUser('alegomes')
		assert user.id == 14147108

	def test_account_existance():
		user = TwitterUser('')
		assert user.existence == False

	# time consuming
	def test_false_account():
		user = TwitterUser('mrinasilv')
		assert user.existence == False


if __name__ == '__main__':
    unittest.main()
