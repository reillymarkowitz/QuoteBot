import tweepy
from tweet_queue import TweetQueue
from bot import QuoteBot

class Tweeter:
    def __init__(self):
        self.bot = QuoteBot()
        self.queue = TweetQueue()

    def tweet(self):
        try:
            quote = self.queue.pop()
            self.bot.tweet(quote)
        except IndexError as err:
            print('No quotes remaining.')

