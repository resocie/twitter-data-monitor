import unittest
import warnings
from twitter.twitter import TwitterUser

class TestTwitterUser(unittest.TestCase):

	def test_name_retrieval(self):
		user = TwitterUser('siqueiralex')
		self.assertEqual('Alex Siqueira', user.name)
	
	def test_id_retrieval(self):
		user = TwitterUser('alegomes')
		self.assertEqual(14147108, user.id)
	
	def test_account_existance(self):
		user = TwitterUser('')
		self.assertEqual(False,user.existence)

	# time consuming	
	def test_false_account(self):
		user = TwitterUser('mrinasilv')
		self.assertEqual(False,user.existence)


if __name__ == '__main__':
    unittest.main()
    