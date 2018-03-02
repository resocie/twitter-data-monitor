import unittest
from twitter.twitter import TwitterUser

class TestTwitterUser(unittest.TestCase):
	def test_isonline(self):
		user = TwitterUser('alegomes')

	def test_name_retrieval(self):
		user = TwitterUser('alegomes')
		self.assertEqual('Alexandre Gomes', user.name)

	def test_id_retrieval(self):
		user = TwitterUser('alegomes')
		self.assertEqual('9999', user.id)
		

if __name__ == '__main__':
    unittest.main()