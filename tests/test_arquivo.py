import unittest
from twitter.twitter import TwitterUser
from twitter.TwitterToolkit import TwitterAPI as Tapi

class TestArquivoCSV(unittest.TestCase):
	def test_arquivo_existe(self):
		try:
			file = open('twitter/autores.csv',newline='')
			file.close()
			arquivo = True
		except:
			arquivo = False
		self.assertEqual(True, arquivo)

	def test_criar_csv(self):
		teste = Tapi.criar_csv_basico()
		self.assertEqual(", teste)

		for user in ['Renova_BR', 'bancadaativista', 'agora_movimento']:
			user = TwitterUser(user)
			teste = Tapi.atualizar_csv_novos_autores(user)

		self.assertEqual("certo", teste)

if __name__ == '__main__':
    unittest.main()
