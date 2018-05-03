import pytest
import warnings
import csv
import os
import modules
from modules.csv_builder import CsvBuilder

class TestFileCSV(unittest.TestCase):
    def test_file_exist():
        try:
            csvfile = open(os.path.join(os.path.dirname(__file__),'../modules/results/autores.csv'))
            csvfile.close()
            arquivo = True
        except:
            arquivo = False
        assert arquivo == True

    def test_create_csv():
        CsvBuilder.create_csv_basic()
        with open(os.path.join(os.path.dirname(__file__),'../modules/results/autores.csv'), 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            row1 = next(reader)
            first_row = ["nome","seguidores","tweets","seguindo","curtidas","hashtags"]
            assert row1 == first_row
            csvfile.close()

    def test_word_separator():
        vector = ['SolidariedadeInternacional', 'DemocratizeJá', 'LulapeloBrasil','DemarcaçãoJá','OcupaCuritiba']
        string = '#SolidariedadeInternacional #DemocratizeJá #LulapeloBrasil #DemarcaçãoJá #OcupaCuritiba '
        hashtags = CsvBuilder.word_separator(vector)
        assert hashtags == string  

if __name__ == '__main__':
    unittest.main()
