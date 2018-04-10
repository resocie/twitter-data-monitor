import unittest
from twitter.twitter import TwitterUser

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
