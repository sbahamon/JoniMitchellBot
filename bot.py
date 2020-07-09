import requests
import tweepy
from os import environ
# import credentials

from genius import *


# local authentication
# consumerKey = credentials.consumerKey
# consumerSecret = credentials.consumerSecret
# twitterApiKey = credentials.twitterApiKey
# twitterApiSecretKey = credentials.twitterApiSecretKey

# heroku authentication
consumerKey = environ['consumerKey']
consumerSecret = environ['consumerSecret']
twitterApiKey = environ['twitterApiKey']
twitterApiSecretKey = environ['twitterApiSecretKey']


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

    api = tweepy.API(auth)
    api.update_status(tweet)
    print("done")




if __name__ == "__main__":
    main()