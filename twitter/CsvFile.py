import csv
import os
from twitter import TwitterUser

class CsvBuilder:

    @staticmethod
    def create_csv_basic():

        with open(os.path.join(os.path.dirname(__file__), 'autores.csv'), 'w+') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow(["nome", "seguidores", "tweets", "seguindo", "curtidas", "hashtags"])
            csvfile.close()

    @staticmethod        
    def update_csv_new_autors(self, username):
        with open(os.path.join(os.path.dirname(__file__),'autores.csv'), 'a') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow([self.name, self.followers_count,
            self.tweets_count, self.following_count, self.likes_count])
            csvfile.close()
