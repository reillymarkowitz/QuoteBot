#!/usr/bin/env python3

import tweepy, nltk, time, os, io
from tweepy.auth import OAuthHandler

# Replace with your own keys
CONSUMER_KEY = 'L6V3C5Ee7Tqi62EGOPBVUaUvE'
CONSUMER_SECRET = 'Qyh4KCFIBpM6MYZi39BHaVnMhKhP5LhnIduWHuU1gczDSexkPG'
ACCESS_TOKEN = '1015305127207559170-oTRJBXqkFpTOnFR3DT8z81ePhN9Guk'
ACCESS_TOKEN_SECRET = 'beSTC1r0BP9Pol88I2rKXx67Rcyi995DlpgamtZHfC5g9'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

BOT_USERNAME = api.me().screen_name
TWEET_LEN = 280
REPLY_LEN = TWEET_LEN - len(BOT_USERNAME) - 2
STARTING_TOKEN = 6519


def tweet(string):
    if string == '.':
        return "ERROR"
    else:
        tweet_id = api.update_status(string).id_str
        print('Tweeted: ' + tweet_id)
        return tweet_id


def reply_to(string, username, tweet_id):
    reply_id = api.update_status('@' + username + ' ' + string, tweet_id).id_str
    print('Replied ' + reply_id + ' to ' + tweet_id)
    return reply_id


def thread(string):
    tweet_id = tweet(string[:TWEET_LEN - 1])
    string = string[TWEET_LEN - 1:]
    while len(string) > REPLY_LEN:
        tweet_id = reply_to(string[:REPLY_LEN], BOT_USERNAME, tweet_id)
        string = string[REPLY_LEN:]
    reply_to(string, BOT_USERNAME, tweet_id)


def main():
    with io.open('ao.txt', 'r', encoding='utf-8') as book_file:
        book_string = book_file.read()

    book_array = nltk.sent_tokenize(book_string)

    for i, token in enumerate(book_array[STARTING_TOKEN:]):
        print('Token # %d' % (i + STARTING_TOKEN))
        if len(token) <= TWEET_LEN:
            tweet(token)
        else:
            thread(token)
        time.sleep(60 * 60)  # Sleep for 60 minutes between tweets

    tweet('End of book. Follow @ReillyMarkowitz for more projects.')
    print('FIN')


try:
    # main()
    print('hello') 
except tweepy.TweepError as e:
    error_code = e[0].code
    if error_code == 187:           # Duplicate status
        print('Status is a duplicate. Attempting to fix...')
        # Implement fix
    else:
        print('An error occurred. (%s)' % code)
except tweepy.RateLimitError:
    print('Slow down!')
