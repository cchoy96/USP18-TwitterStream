import tweepy
import json
import sys
import time

# Christopher Choy
# USP18 - HW5, Problem 2

# f = open('tweetstream_out.txt', 'a', 0)
# f2 = open('tweetstream_ids.txt', 'a', 0)
timelimit = 300 #seconds
keywords = ['information security', 'information privacy']
keywords2 = ['information security', 'information privacy', 'data science',
	'data security', 'privacy policy', 'cyber security', 'customer data', 'blase ur']
	
# override tweepy.StreamListener to add on_status logic
class MyStreamListener(tweepy.StreamListener):
	def __init__(self, time_limit=60):
		self.start_time = time.time()
		self.limit = time_limit
		self.saveFile = open('saveFile.json', 'a', 0)
		super(MyStreamListener, self).__init__()

	def on_data(self, data):
		if (time.time() - self.start_time) < self.limit:
			print(json.loads(data)['text'])
			self.saveFile.write(data)
			return True
		else:
			self.saveFile.close()
			return False

	# def on_status(self, status):
	# 	try:
	# 		print(status.id, status.text)
	# 		f.write(status.text + '\n\n')
	# 		f.flush()
	# 		f2.write(status.id)
	# 		f2.flush()
	# 		print 'here'
	# 	except:
	# 		pass # ignore errors to prevent breaking app

	def on_error(self, status_code):
		if status_code == 420:
			return False 	# disconnects stream

# These shouldn't be human readable or distributed, but here they are
consumer_key 		= ''
consumer_secret 	= ''
access_token 		= ''
access_token_secret 	= ''

# OAuth Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Listen to the Stream
myStreamListener = MyStreamListener(time_limit=timelimit)
stream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

stream.filter(track=keywords, languages=['en'], encoding='utf-8', filter_level='low')
# f.close()
# f2.close()
print('\n-----------\nScript Complete!')
