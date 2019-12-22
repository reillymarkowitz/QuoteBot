import io, csv, time, sys, argparse, tweepy
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


with open('tokenized_tweets.csv', 'rt') as quoteFile:
    reader = csv.reader(quoteFile)
    bot = QuoteBot()
    
    # Skip over the first
    # START_QUOTE rows
    for i in range(START_QUOTE):
        next(reader)

    for i, row in enumerate(reader):
        quote = row[0]
        print('Tweeting quote #%d...' % (i + START_QUOTE))

        try:
            bot.tweet(quote)
        except tweepy.TweepError as e:
            error_code = e.message[0]['code']
            
            if error_code == 187:
                print('Duplicate tweet. Skipping to the next one...')
                continue
            else:
                print(e)

        time.sleep(60 * 60 * WAIT_TIME)

print('No quotes remaining.')

