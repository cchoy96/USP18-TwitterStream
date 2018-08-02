import requests, urllib
import base64
import json

# Consumer Key & Secret
key = 'brwJsKyVQHqCtOJMMxK7n9PYk'
secret = '5EfrIRixXPfCzkjsgzcamoVvU6s6hx2KCIZeJGFAB9eC7L9pn1'


# https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
def getBearerToken() :
	# Encode Consumer Key and Secret
	stringToEncode = key + ':' + secret
	bearer_credentials = base64.b64encode(stringToEncode)

	# Obtain Bearer Token
	url_oauth = "https://api.twitter.com/oauth2/token"
	auth 	  = 'Basic ' + bearer_credentials
	content   = 'application/x-www-form-urlencoded;charset=UTF-8'
	hdrs  	  = {'Authorization':auth,'Content-Type':content}
	payload   = {'grant_type':'client_credentials'}

	r = requests.post(url_oauth, headers=hdrs, params=payload)
	parsed_json = json.loads(json.dumps(r.json()))

	if parsed_json['token_type'] == 'bearer':
		bearer_token = parsed_json['access_token']
	else:
		print('Access token not returned')
		sys.exit()

	# Authenticate API Requests with Bearer Token
	return bearer_token

def streamTwitter(bearer_token):
	url = 'https://stream.twitter.com/1.1/statuses/filter.json'
	hdrs = {'Authorization':'Bearer '+bearer_token}
	keywords = 'information privacy, information security, privacy, data security, IoT'
	data={'track':keywords, 'language':'en'}

	r = requests.get(url, headers=hdrs, params=data)
	print r

def main():
	streamTwitter(getBearerToken())
	print 'script complete'

main()

