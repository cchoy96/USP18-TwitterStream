import tweepy
import json
import sys
import time

# Christopher Choy
# USP18 - HW5, Problem 2

fout = 'saveFile.json'
timelimit = 28800 #seconds. 8hrs = 28800
filter_lvl = 'none'
keywords = ['information security', 'information privacy', 'data science', 'data security', 'privacy policy', 'customer data', 'blase ur']

# override tweepy.StreamListener to add on_status logic
class MyStreamListener(tweepy.StreamListener):
	def __init__(self, time_limit=60):
		self.start_time = time.time()
		self.limit = time_limit
		self.saveFile = open(fout, 'a', 0)
		super(MyStreamListener, self).__init__()

	def on_data(self, data):
		if (time.time() - self.start_time) < self.limit:
			print(json.loads(data)['text'] + '\n========')
			self.saveFile.write(data)
			return True
		else:
			self.saveFile.close()
			return False

	def on_error(self, status_code):
		if status_code == 420:
			return False 	# disconnects stream

# These shouldn't be human readable or distributed, but here they are
consumer_key 		= 'brwJsKyVQHqCtOJMMxK7n9PYk'
consumer_secret 	= '5EfrIRixXPfCzkjsgzcamoVvU6s6hx2KCIZeJGFAB9eC7L9pn1'
access_token 		= '565659325-jVylfIP8JRIV2Jf49a9kGFd7GOmWFdyi5eSMzFLM'
access_token_secret = 'LlvfHxwXCs6nT42Dmtq8CFuosNYgbwTFPhlwhqlzHy5MY'

# OAuth Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Listen to the Stream
print('Streaming tweets for ' + str(timelimit/60) + ' minutes...')
myStreamListener = MyStreamListener(time_limit=timelimit)
stream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
stream.filter(track=keywords, languages=['en'], encoding='utf-8', filter_level=filter_lvl)

print('\n\nScript Complete!')
