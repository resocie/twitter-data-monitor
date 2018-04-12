import csv
from twitter.twitter import TwitterUser

class CsvBuilder:

    def create_csv_basic():
        with open('twitter/autores.csv', 'w') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow(["nome", "seguidores", "tweets", "seguindo", "curtidas"])
            csvfile.close()

    def update_csv_new_autors(self, username):
        with open('twitter/autores.csv', 'a') as csvfile:
            writer_t = csv.writer(csvfile, delimiter=';')
            writer_t.writerow([self.name, self.followers_count,
            self.tweets_count, self.following_count, self.likes_count])
            csvfile.close()
