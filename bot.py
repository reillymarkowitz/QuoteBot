#!/usr/bin/env python3

import tweepy, os 
from tweepy.auth import OAuthHandler
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

if API_KEY is None:
    raise ValueError('Failed to read API_KEY from .env')

if API_SECRET is None:
    raise ValueError('Failed to read API_SECRET from .env')

if ACCESS_TOKEN is None:
    raise ValueError('Failed to read ACCESS_TOKEN from .env')

if ACCESS_TOKEN_SECRET is None:
    raise ValueError('Failed to read ACCESS_TOKEN_SECRET from .env')

class QuoteBot:

    def __init__(self):
        auth = OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

        self.username = self.api.me().screen_name
        self.max_tweet_len = 270 # the limit is 280 but twitter counts some characters as 2
        self.max_reply_len = self.max_tweet_len - len(self.username) - 2

        
    def tweet(self, string):
        if len(string) <= self.max_tweet_len:
            return self.api.update_status(string).id_str

        self.thread(string)

    
    def thread(self, string):
        tweet_id = self.tweet(string[:self.max_tweet_len])
        string = string[self.max_tweet_len:]

        while len(string) > self.max_reply_len:
            reply = '@' + self.username + ' ' + string[:self.max_reply_len]
            tweet_id = self.api.update_status(reply, tweet_id).id_str
            string = string[self.max_reply_len:]

        reply = '@' + self.username + ' ' + string
        self.api.update_status(reply, tweet_id)

