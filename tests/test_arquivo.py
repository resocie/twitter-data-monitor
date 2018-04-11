import unittest
from twitter.twitter import TwitterUser
from twitter.TwitterToolkit import TwitterAPI as Tapi

class TestFileCSV(unittest.TestCase):
	def test_file_exist(self):
		try:
			file = open('twitter/autores.csv',newline='')
			file.close()
			arquivo = True
		except:
			arquivo = False
		self.assertEqual(True, arquivo)

	def test_create_csv(self):
		teste = Tapi.create_csv_basic()
		self.assertEqual("", teste)

		for user in ['Renova_BR', 'bancadaativista', 'agora_movimento']:
			user = TwitterUser(user)
			teste = Tapi.update_csv_new_autors(user)

		self.assertEqual("certo", teste)

if __name__ == '__main__':
    unittest.main()
