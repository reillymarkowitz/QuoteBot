import requests, re
from bs4 import BeautifulSoup
from random import shuffle
from tweet_queue import TweetQueue
from typing import List

AUTHOR_QUOTE_URL = 'https://www.goodreads.com/author/quotes/13009.Gilles_Deleuze'

class Scraper:
    def __init__(self):
        self.params = {'page' : 1}

    def scrape(self) -> None:
        quotes = self.getQuotes()
        self.enqueueQuotes(quotes)

    def getQuotes(self) -> List[str]:
        quotes = []
        while True:
            print('Scraping page', self.params['page'], '...')

            res = requests.get(url = AUTHOR_QUOTE_URL, params = self.params)
            parser = BeautifulSoup(res.text, 'html.parser')
            quoteTags = parser.findAll('div', {'class': 'quoteText'})

            # break out of the loop when no quotes
            # are found on the current page
            if len(quoteTags) == 0:
                print('No quotes on page', self.params['page'])
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

            self.params['page'] += 1

        return quotes

    def enqueueQuotes(self, quotes: List[str]) -> None:
        shuffle(quotes)
        queue = TweetQueue()
        queue.push(quotes)

