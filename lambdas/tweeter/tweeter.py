import tweepy
from scraper.tweet_queue import TweetQueue
from bot import QuoteBot

bot = QuoteBot()
queue = TweetQueue()

try:
    quote = queue.pop()
    bot.tweet(quote)
except IndexError as err:
    print('No quotes remaining.')

