import json

# Create array of json objects from file
data = []
with open('saveFile.json', 'r') as f:
	for line in f:
		data.append(json.loads(line))

# Write tweets to a file
print("Writing tweets.txt...")
with open('tweets.txt', 'w') as f:
	for tweet in data:
		f.write(tweet['text'].encode('utf-8') + '\n========\n')

# Filter and Create Words Array
words = []
for tweet in data:
	# print(tweet['id'])
	strlist = tweet['text'].encode('utf-8').split()
	for word in strlist:
		if word[0] == '@': continue
		elif word[:4] == 'http': continue
		else:
			words.append(word)

# Write words to a file
print("Writing words.txt...")
with open('words.txt', 'w') as f:
	for word in words:
		f.write(word + '\n')

print("Script Complete.")