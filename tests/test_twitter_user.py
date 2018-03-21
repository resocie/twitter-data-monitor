import unittest
from twitter.twitter import TwitterUser

class TestTwitterUser(unittest.TestCase):
	def test_isonline(self):
		user = TwitterUser('siqueiralex')

	def test_name_retrieval(self):
		user = TwitterUser('alegomes')
		self.assertEqual('Alexandre Gomes', user.name)
		user = TwitterUser('siqueiralex')
		self.assertEqual('Alex Siqueira', user.name)

	def test_id_retrieval(self):
		user = TwitterUser('alegomes')
		self.assertEqual(14147108, user.id)
		user = TwitterUser('siqueiralex')
		self.assertEqual(52126452, user.id)
			




if __name__ == '__main__':
    unittest.main()