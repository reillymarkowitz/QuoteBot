#!/usr/bin/env python3

import nltk, csv

bookPath = 'ao.txt'

with open(bookPath, 'r') as bookFile:
    bookString = bookFile.read()

tweets = nltk.sent_tokenize(bookString)

tweetFile = csv.writer(open('tokenized_tweets.csv', 'w')) 

for tweet in tweets:
    tweetFile.writerow([tweet])

