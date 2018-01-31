import tweepy

consumer_key = 'LiCjuL9KOI36y78Mbtlr4GxIn'
consumer_secret = 'oZrMJ97fqanwtcOqiMYqkyFdbAt2ELRwcH3pU3WbrB9nUHsm6b'
access_token = '956408944603185153-lPWJtUzYVeZRVoIjsrLOTg92Z96NT75'
access_secret = 'ZSuIGpuQ6aF5EARezGcJqMHxHX11U5F7mr1PO5V5NC16g'

OAUTH_KEYS = {'consumer_key':consumer_key, 'consumer_secret':consumer_secret, 'access_token_key':access_token, 'access_token_secret':access_secret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

ransomware = tweepy.Cursor(api.search, q='ransomware').items(10)

for tweet in ransomware:
   print tweet.created_at, tweet.text, tweet.lang