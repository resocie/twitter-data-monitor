# modulo criado para "brincar" com a api

from twitter import TwitterUser

bolson = TwitterUser('jairbolsonaro')
print bolson.name
print "seguidores: " + str(bolson.followers_count)
print "tweets: "+ str(bolson.tweets_count)
print "seguindo: "+ str(bolson.following_count)
