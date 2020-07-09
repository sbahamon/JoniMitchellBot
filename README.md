# Joni Mitchell Bot at @DoseOfJoni

Twitter bot meant to tweet random Joni Mitchell lyrics every hour on the half hour.
Please feel free to fork this project and use it for your own twitter lyrics bot!

## Built With

Bot is build in Python 3 using the following packages:
 - Tweepy for twitter authentication
 - Requests for http requesting from the Genius API
 - Beautiful Soup for scraping lyrics
 - Flask for deploying a web server to use the worker on Heroku
Lyrics are from the Genius API.
Bot is deployed and scheduled on Heroku.

## How it works

Helper functions are saved in genius.py to scrape for songs from Joni Mitchell and lyrics from those songs.
Song IDs for the Genius API were previously scraped and saved in songs.py as a list. 
A random song ID from this list is selected everytime bot.py runs to construct the tweet.

## How to run locally with artist of your choice

First you need to collect the song IDs for the artist of your choice.

1. Fork & clone this repo and run `python3 -m pip install -r requirements.txt`. I recommend using a virtual environment as outlined in [this Python documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 
2. Create a `credentials.py` file in the directory containing this repo and add a line containing your Genius API token like so:
   `geniusToken = "INSERT_TOKEN_HERE"`
3. Uncomment [Line 8](https://github.com/sbahamon/JoniMitchellBot/blob/main/genius.py#L8) and [Line 17](https://github.com/sbahamon/JoniMitchellBot/blob/main/genius.py#L17) and comment out [Line 20](https://github.com/sbahamon/JoniMitchellBot/blob/main/genius.py#L20) in `genius.py`.
4. Replace [Line 25](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L25) in `bot.py` with the artist ID for the artist of your choice. To find the artist ID, I recommend using the search function of the genius API to search for an artist: after that, you can check the responses and look for the ID of the artist in the returned JSON.
5. Uncomment [Lines 28 to 30](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L28-30) and comment out [Lines 32 to 42](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L32-42) in `bot.py`. 
6. Run the script using `python3 bot.py`

After that, you should have a list of song IDs in `songs.py`. Open this file, append `songs = ` before the start of the list, save, and close the file. 
To generate a tweet using lyrics randomly selected from one of the song IDs in your new `songs.py` list:

1. Uncomment [Line 4](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L4), [Lines 10 to 13](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L10-13), and [Lines 32 to 42](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L32-42) and comment out [Lines 16 to 19](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L16-19) and [Lines 28 to 30](https://github.com/sbahamon/JoniMitchellBot/blob/main/bot.py#L28-30) in `bot.py`. 
2. In your `credentials.py` file, add 4 lines with your Twitter authentication information like so:
   ```
   consumerKey = "INSERT"
   consumerSecret = "YOURS"
   twitterApiKey = "RIGHT"
   twitterApiSecretKey = "HERE"
   ```
3. Rerun the script with `python3 bot.py` 


## Useful Links

Following webpages were used as technical guides and models for the creation of this bot:
 - Guides:
    - [Real Python](https://realpython.com/twitter-bot-python-tweepy/)
    - [FreeCodeCamp](https://www.freecodecamp.org/news/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607/)
    - [Twilio](https://www.twilio.com/blog/build-deploy-twitter-bots-python-tweepy-pythonanywhere)
    - [DevTo](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39)
    - [ANOVAProject](https://github.com/ANOVAProjectUSYD/lyrics-analysis)
 - Models:
   - [Mrouru's LyricsBot](https://github.com/mrouru/LyricsBot)
   - [Sam Kravit's PhishBot](https://github.com/samkravitz/PhishBot)