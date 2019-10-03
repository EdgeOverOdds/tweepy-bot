import tweepy
import logging
import time

from config import create_api  # file we created

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow_followers(api):
    logger.info('retreiving and following followers')
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Following {follower.name}")
            follower.follow()


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info("Waiting...")
        time.sleep(60)  # calls this once every minute. stop with "CRTL + C"


if __name__ == "__main__":
    main()