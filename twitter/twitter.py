from twitter.TwitterToolkit import TwitterAPI, TweetTK

class TwitterUser:

	def __init__(self,username):
		api = TwitterAPI()
		if username != '':
			try:
				user = api.get_user(username)
				self.existence = True
				self.id = user.id
				self.username = user.screen_name
				self.name = user.name
				self.followers_count = user.followers_count
				self.tweets_count = user.statuses_count
				self.following_count = user.friends_count
				self.likes_count = user.favourites_count
			except Exception as e:
				self.existence = False
		else:
			self.existence = False
			
	def last_month_hashtags(self,num_months=1):
		api = TwitterAPI()
		tweets = api.get_user_last_month_tweets(self.username, num_months)
		hashtags = TweetTK.extract_hashtags(tweets)
		return hashtags

	def hashtags_from(self, day, month, year):
		api = TwitterAPI()
		tweets = api.get_user_tweets_from(self.username, day, month, year)
		hashtags = TweetTK.extract_hashtags(tweets)
		return hashtags	
	