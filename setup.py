#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests, re, nltk, csv

AUTHOR_QUOTE_URL = 'https://www.goodreads.com/author/quotes/13009.Gilles_Deleuze'
PARAMS = {'page' : 1}

quotes = []

while True:
    print('Scraping page', PARAMS['page'])

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
            quote = re.search('\“.+\”', contents)[0]
            formattedQuote = '\"' + quote[1:-1] + '\"'
            quotes.append(formattedQuote)
        except TypeError:
            # thrown when no match is found
            continue

    PARAMS['page'] += 1


tweetFile = csv.writer(open('tokenized_tweets.csv', 'w')) 

for quote in quotes:
    tweetFile.writerow([quote])

'''

bookPath = 'ao.txt'

with open(bookPath, 'r') as bookFile:
    bookString = bookFile.read()

tweets = nltk.sent_tokenize(bookString)

tweetFile = csv.writer(open('tokenized_tweets.csv', 'w')) 

for tweet in tweets:
    tweetFile.writerow([tweet])
'''
