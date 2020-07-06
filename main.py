import tweepy
from scraper.tweet_queue import TweetQueue
from bot import QuoteBot

bot = QuoteBot()
queue = TweetQueue()

for i in range(START_QUOTE, len(quotes)):
    print('Tweeting quote #%d...' % i)

    try:
        quote = queue.pop()
        bot.tweet(quote)
    except tweepy.TweepError as err:
        if err.api_code == 187:
            print('Duplicate tweet. Skipping to the next one...')
            continue
        else:
            raise err

    time.sleep(60 * 60 * WAIT_TIME)

print('No quotes remaining.')

