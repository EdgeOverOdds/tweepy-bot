'''
will require articles to be generated from a system running a GPU
I am using google colab for this purpose, and building a corpus of articles to post

For Grover, borrowing heavily from tutorial and google colab code
tutorial: https://medium.com/@ageitgey/deepfaking-the-news-with-nlp-and-transformer-models-5e057ebd697d
colab notebook: https://colab.research.google.com/drive/1VI3oBIOQYsym2x5oOux7DTNhpdR0r4uw#scrollTo=uvGg4QZB-ZxX

'''


import tweepy
import json
import logging
from config import create_api
import time
import pickle
import random

#setup logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()


def read_in_articles_json(file):
    with open(file, 'rb') as f:
        try:
            itemlist = json.load(f)
            logger.info(f" read in {(len(itemlist))} articles")
        except:
            logger.info(f" did not work")
    return itemlist
            

def post_tweets(api, article):
    api = api
    tweets = api.user_timeline()
    if article['text'] not in tweets:
        #logger.info(f' Tweeting {article['title']}')
        print(len(article['text']))
        try:
            post_info = article['text'][:270]
            post_title = article['title']
            api.update_status(post_info)             #the tweet!
            logger.info(f' posting article {post_title}')
            logger.info("Waiting...")
            time.sleep(60)  # will need to stop manually, could also randomize this a bit
        except:
            logger.info(f'not tweeting ,  as it was already posted')


def main():
    #create the api
    api = create_api()

    #read in the articles
    articles = read_in_articles_json('../articles_colab.txt')

    while True:
        for article in articles:
            post_tweets(api, article)


        
if __name__ == "__main__":
    main()


    


