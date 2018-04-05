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
		self.assertEqual(14147108, user.id)

class TestArquivoCSV(unittest.TestCase):
	def test_arquivo_existe(self):
		try:
			file = open('twitter/autores.csv',newline='')
			file.close()
			arquivo = True
		except:
			arquivo = False
		self.assertEqual(True, arquivo)


if __name__ == '__main__':
    unittest.main()
