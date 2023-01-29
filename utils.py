import logging as log
import string
from urllib.request import urlopen

log.basicConfig(level=log.DEBUG)


def wait_for_internet_connection():
    test_url: string = 'https://www.google.com'
    while True:
        try:
            # Random url to check for internet connection
            urlopen(test_url, timeout=1)
            log.info("Internet connection obtained!")
            return
        except Exception as e:
            log.info("could not obtain internet connection")
        pass
