import requests
import tweepy
from os import environ
import credentials as cd

# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']


# Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(cd.CONSUMER_KEY, cd.CONSUMER_SECRET)
auth.set_access_token(cd.ACCESS_KEY, cd.ACCESS_SECRET)

# Create API object
api = tweepy.API(auth)

# Create a tweet
# api.update_status("is this thing on")
# print("done")