import unittest
import csv
from twitter.CsvFile import CsvBuilder
from twitter.TwitterToolkit import TwitterAPI as Tapi

class TestFileCSV(unittest.TestCase):
    def test_file_exist(self):
        try:
            csvfile = open('twitter/autores.csv',newline='')
            csvfile.close()
            arquivo = True
        except:
        	arquivo = False
        self.assertEqual(True, arquivo)

    def test_create_csv(self):
        CsvBuilder.create_csv_basic()
        with open('twitter/autores.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            row1 = next(reader)
            first_row = ["nome","seguidores","tweets","seguindo","curtidas","hashtags"]
            self.assertEqual(first_row,row1)
            csvfile.close()

if __name__ == '__main__':
    unittest.main()
