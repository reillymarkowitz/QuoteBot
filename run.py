import tweepy
import nltk
import time
import os

nltk.download('punkt')

# Replace with your own keys
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

BOT_USERNAME = api.me().screen_name
TWEET_LEN = 280
REPLY_LEN = TWEET_LEN - len(BOT_USERNAME) - 2


def tweet(string):
    tweet_id = api.update_status(string).id_str
    print('Tweeted: ' + tweet_id)
    return tweet_id


def reply_to(string, username, tweet_id):
    reply_id = api.update_status('@' + username + ' ' + string, tweet_id).id_str
    print('Replied ' + reply_id + ' to ' + tweet_id)
    return reply_id


def thread(string):
    tweet_id = tweet(string[:TWEET_LEN])
    string = string[TWEET_LEN:]
    while len(string) > REPLY_LEN:
        tweet_id = reply_to(string[:REPLY_LEN], BOT_USERNAME, tweet_id)
        string = string[REPLY_LEN:]
    reply_to(string, BOT_USERNAME, tweet_id)


book_file = open('ao.txt', 'r')  # Replace with path to your file
book_string = book_file.read()
book_array = nltk.sent_tokenize(book_string)  # Convert text into array of sentences

for sentence in book_array:
    if len(sentence) <= TWEET_LEN:
        tweet(sentence)
    else:
        thread(sentence)
    time.sleep(30 * 60)  # Sleep for 30 minutes between tweets

tweet('End of book. Follow @ReillyMarkowitz for more projects.')
print('FIN')
