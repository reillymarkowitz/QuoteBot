import boto3, json
from typing import List

class TweetQueue:
    def __init__(self):
        s3 = boto3.resource('s3')
        self.quoteFile = s3.Object('quotebot-quotes', 'quotes.json')

    def push(self, tweets: List[str]) -> None:
        tweetsJson = json.dumps(tweets).encode('UTF-8')
        self.quoteFile.put(
            Body = bytes(tweetsJson)
        )

    def pop(self) -> str:
        quoteData = self.quoteFile.get()['Body'].read().decode('UTF-8')
        quotes = json.loads(quoteData)

        if len(quotes) == 0:
            raise IndexError('Cannot pop from empty queue')

        first, rest = quotes[0], quotes[1:]
        self.push(rest)

        return first

