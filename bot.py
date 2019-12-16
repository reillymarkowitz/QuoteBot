#!/usr/bin/env python3

import tweepy, os 
from tweepy.auth import OAuthHandler
from dotenv import load_dotenv

load_dotenv()

# Replace with your own keys
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')


class QuoteBot:

    def __init__(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

        self.username = self.api.me().screen_name
        self.max_tweet_len = 280
        self.max_reply_len = self.max_tweet_len - len(self.username) - 2

        
    def tweet(self, string):
        if len(string) <= self.max_tweet_len:
            return self.api.update_status(string).id_str

        self.thread(string)

    
    def thread(self, string):
        tweet_id = self.tweet(string[:self.max_tweet_len - 1])
        string = string[self.max_tweet_len - 1:]

        while len(string) > self.max_reply_len:
            reply = '@' + self.username + ' ' + string[:self.max_reply_len]
            tweet_id = self.api.update_status(reply, tweet_id).id_str
            string = string[self.max_reply_len:]

        reply = '@' + self.username + ' ' + string
        self.api.update_status(reply, tweet_id)

