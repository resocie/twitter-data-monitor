import json
from twitter.TwitterToolkit import TwitterAPI, TweetTK
from twitter.twitter import TwitterUser
from twitter.CsvFile import CsvBuilder


if __name__ == '__main__':
    file = open("helpers/politicians.json")
    actors = json.load(file)
    for row in actors:
        user = TwitterUser(row["twitter_handle"])
        if user.existence == True:
            CsvBuilder.update_csv_new_autors(user)
