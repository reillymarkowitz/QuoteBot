import io, csv, time, sys, argparse, tweepy, json
from bot import QuoteBot

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


quoteFile = open('quotes.json', 'r')
quotes = json.loads(quoteFile.read())
bot = QuoteBot()

for i in range(START_QUOTE, len(quotes)):
    print('Tweeting quote #%d...' % i)

    try:
        bot.tweet(quotes[i])
    except tweepy.TweepError as err:
        if err.api_code == 187:
            print('Duplicate tweet. Skipping to the next one...')
            continue
        else:
            raise err

    time.sleep(60 * 60 * WAIT_TIME)

print('No quotes remaining.')

