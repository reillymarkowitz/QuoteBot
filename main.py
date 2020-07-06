import io, csv, time, sys, argparse, tweepy
from bot import QuoteBot
from scraper.tweet_queue import TweetQueue

parser = argparse.ArgumentParser()

parser.add_argument(
        '-s',
        '--start', 
        type = int, 
        default = 0,
        help = 'quote number to begin with (default 0)'
    )

parser.add_argument(
        '-i', 
        '--interval', 
        type = int, 
        default = 12,
        help = 'time between tweets in hours (default 12)'
    )

options = parser.parse_args(sys.argv[1:])

START_QUOTE = options.start
WAIT_TIME = options.interval

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

