import requests, re
from bs4 import BeautifulSoup
from random import shuffle
from tweet_queue import TweetQueue

AUTHOR_QUOTE_URL = 'https://www.goodreads.com/author/quotes/13009.Gilles_Deleuze'
PARAMS = {'page' : 1}
quotes = []

while True:
    print('Scraping page', PARAMS['page'], '...')

    res = requests.get(url = AUTHOR_QUOTE_URL, params = PARAMS)
    parser = BeautifulSoup(res.text, 'html.parser')
    quoteTags = parser.findAll('div', {'class': 'quoteText'})

    # break out of the loop when no quotes
    # are found on the current page
    if len(quoteTags) == 0:
        print('No quotes on page', PARAMS['page'])
        print('Done scraping.')
        break

    for tag in quoteTags:
        try:
            contents = tag.contents[0]
            match = re.search('\“(.+)\”', contents)
            quote = match[1]
            if quote[0] != '\"' and quote[-1] != '\"':
                quote = '\"' + quote + '\"'
            quotes.append(quote)
        except TypeError:
            # thrown when no match is found
            continue

    PARAMS['page'] += 1


shuffle(quotes)
queue = TweetQueue()
queue.push(quotes)
