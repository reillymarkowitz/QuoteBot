#!/usr/bin/env python3

import io, csv, time
from bot import QuoteBot

START_QUOTE = 0
WAIT_TIME = 12

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
