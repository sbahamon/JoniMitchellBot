import requests
import tweepy
from os import environ
import credentials as cd

from genius import *


# local authentication
consumerKey = credentials.consumerKey
consumerSecret = credentials.consumerSecret
twitterApiKey = credentials.twitterApiKey
twitterApiSecretKey = credentials.twitterApiSecretKey

# heroku authentication
# CONSUMER_KEY = environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']


def main():
    # Example searches
    term = 'Joni Mitchell'
    artist_id = 989

    # Grabs all song id's from artist and saves them to text file
    # songs = get_song_id(989)
    # with open('songs.txt', 'w') as outfile:
    #     json.dump(songs, outfile)

    lucky_song = random.randint(1,277)
    tweet = get_lyrics_tweet(retrieve_lyrics(songs[lucky_song]))
    print(tweet)

    # local authentication
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(twitterApiKey, twitterApiSecretKey)

    # heroku authentication
    # auth = tweepy.OAuthHandler(cd.CONSUMER_KEY, cd.CONSUMER_SECRET)
    # auth.set_access_token(cd.ACCESS_KEY, cd.ACCESS_SECRET)

    api = tweepy.API(auth)
    api.update_status(tweet)
    print("done")




if __name__ == "__main__":
    main()