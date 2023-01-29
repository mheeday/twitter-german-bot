import os
import string
from urllib.request import urlopen

import tweepy
import logging
import schedule
import time

from utils import wait_for_internet_connection

logging.basicConfig(level=logging.DEBUG)

consumer_key: string = os.environ.get("CONSUMER_KEY")
consumer_secret: string = os.environ.get("CONSUMER_SECRET")
access_token: string = os.environ.get("ACCESS_TOKEN")
access_token_secret: string = os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token: string = os.environ.get("BEARER_TOKEN")

tw2 = tweepy.Client(bearer_token,
                    consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)

tw1_auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

tw1_api = tweepy.API(tw1_auth)


def scheduled_test():
    wait_for_internet_connection();
    logging.info("Got")


schedule.every(10).seconds.do(scheduled_test)


while True:
    schedule.run_pending()
    time.sleep(1)