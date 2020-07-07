from tweeter import Tweeter

def handler(event, context):
    tweeter = Tweeter()
    tweeter.tweet()
