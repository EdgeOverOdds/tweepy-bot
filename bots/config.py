import tweepy
import logging
import os
import json

logger = logging.getLogger()

file = '../credentials.txt'
with open(file, 'r') as f:
    dict1 = json.loads(f.read())


def create_api():
    consumer_key = dict1['api_key']
    consumer_secret = dict1['api_secret_key']
    access_token = dict1['access_token']
    access_token_secret = dict1['access_token_secret']

    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error calling API', exc_info=True)
        raise e
    logger.info('API Created')
    return api
