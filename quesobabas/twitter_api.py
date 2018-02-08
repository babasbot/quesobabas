import logging

logging.basicConfig(level=logging.INFO)

import os
import tweepy

def auth_twitter_api():
    consumer_key        = os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret     = os.environ["TWITTER_CONSUMER_SECRET"]
    access_token        = os.environ["TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth

auth = auth_twitter_api()
api  = tweepy.API(auth)
