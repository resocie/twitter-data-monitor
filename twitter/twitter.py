from twitter.TwitterToolkit import TwitterAPI, TweetTK

class TwitterUser:

	def __init__(self,username):
		api = TwitterAPI()
		user = api.get_user(username)

		self.id = user.id
		self.username = user.screen_name
		self.name = user.name
		self.followers_count = user.followers_count
		self.tweets_count = user.statuses_count
		self.following_count = user.friends_count

	def last_month_hashtags(self,num_months=1):
		api = TwitterAPI()
		tweets = api.get_user_last_month_tweets(self.username, num_months)
		hashtags = TweetTK.extract_hashtags(tweets)
		return hashtags
