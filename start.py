#!/usr/bin/env python3

import tweepy, nltk, time, os, io, csv
from tweepy.auth import OAuthHandler
from dotenv import load_dotenv

load_dotenv()

# Replace with your own keys
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

BOT_USERNAME = api.me().screen_name
MAX_TWEET_LEN = 280
REPLY_LEN = MAX_TWEET_LEN - len(BOT_USERNAME) - 2
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
    tweet_id = tweet(string[:MAX_TWEET_LEN - 1])
    string = string[MAX_TWEET_LEN - 1:]
    while len(string) > REPLY_LEN:
        tweet_id = reply_to(string[:REPLY_LEN], BOT_USERNAME, tweet_id)
        string = string[REPLY_LEN:]
    reply_to(string, BOT_USERNAME, tweet_id)


def main():
    with io.open('ao.txt', 'r', encoding='utf-8') as book_file:
        book_string = book_file.read()

    try:
        book_array = nltk.sent_tokenize(book_string)

        for i, token in enumerate(book_array[STARTING_TOKEN:]):
            print('Token # %d' % (i + STARTING_TOKEN))
            if len(token) <= MAX_TWEET_LEN:
                tweet(token)
            else:
                thread(token)
            time.sleep(60 * 60)  # Sleep for 60 minutes between tweets

        tweet('End of book. Follow @ReillyMarkowitz for more projects.')
        print('FIN')
    except LookupError:
        print('ERROR: Please run setup.py before start.py.')


try:
    # main()
    with open('tokenized_tweets.csv', 'rt') as quoteFile:
        for row in csv.reader(quoteFile):
            quote = row[0]
            print(quote)

except tweepy.TweepError as e:
    error_code = e.message[0]['code']

    # Duplicate status error
    if error_code == 187: 
        print('Status is a duplicate. Attempting to fix...')
        # Implement fix
    else:
        print('An error occurred. (%s)' % code)
except tweepy.RateLimitError:
    print('Slow down!')
