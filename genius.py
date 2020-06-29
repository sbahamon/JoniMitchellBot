import requests
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import random

import credentials
from songs import songs


# Constants
base = "https://api.genius.com"
client_access_token = credentials.geniusToken

def get_json(path, params=None, headers=None):
    '''Send request and get response in json format.'''

    # Generate request URL
    requrl = '/'.join([base, path])
    token = "Bearer {}".format(client_access_token)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    # Get response object from querying genius api
    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

def connect_lyrics(song_id):
    '''Constructs the path of song lyrics.'''
    url = "songs/{}".format(song_id)
    data = get_json(url)

    # Gets the path of song lyrics
    path = data['response']['song']['path']

    return path


def retrieve_lyrics(song_id):
    '''Retrieves lyrics from html page.'''
    path = connect_lyrics(song_id)

    URL = "http://genius.com" + path
    page = requests.get(URL)

    # Extract the page's HTML as a string
    html = BeautifulSoup(page.text, "html.parser")

    # Scrape the song lyrics from the HTML
    lyrics = html.find("div", class_="lyrics").get_text()
    return lyrics


def get_song_id(artist_id):
    '''Get all the song id from an artist.'''
    current_page = 1
    next_page = True
    songs = [] # to store final song ids

    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page} # the current page
        data = get_json(path=path, params=params) # get json of songs

        page_songs = data['response']['songs']
        # print(page_songs)
        if page_songs:
            # Add all the songs of current page
            songs += page_songs
            # Increment current_page value for next loop
            current_page += 1
            print("Page {} finished scraping".format(current_page))
            # If you don't wanna wait too long to scrape, un-comment this
            # if current_page == 2:
            #     break

        else:
            # If page_songs is empty, quit
            next_page = False

    print("Song id were scraped from {} pages".format(current_page))

    # Get all the song ids, excluding not-primary-artist songs.
    songs = [song for song in songs
            if song["primary_artist"]["id"] == artist_id]

    songs_ids_only = [song["id"] for song in songs
        if song["primary_artist"]["id"] == artist_id]

    return songs_ids_only

def get_lyrics_tweet(lyrics):
    '''Constructs random tweet from random song'''
    lyrics = lyrics.replace('\n\n', '\n')
    lines = lyrics.count('\n')
    start = random.randint(1,lines)
    tweet = ""
    while (len(tweet) < 140) and (start < lines) :
        tweet += lyrics.splitlines()[start] + "\n"
        start += 1

    print(tweet)
    print(len(tweet))

    return tweet


def main():
    # Example searches
    term = 'Joni Mitchell'
    artist_id = 989

    # Grabs all song id's from artist and saves them to text file
    # songs = get_song_id(989)
    # with open('songs.txt', 'w') as outfile:
    #     json.dump(songs, outfile)

    lucky_song = random.randint(1,277)
    # print(songs[lucky_song])
    # print(retrieve_lyrics(songs[lucky_song]))
    get_lyrics_tweet(retrieve_lyrics(songs[lucky_song]))



    # Get meta information about songs
    #song_list = get_song_information(songs_ids)




if __name__ == "__main__":
    main()