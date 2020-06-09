#!/usr/bin/env python3
from time import sleep
from requests import get
from requests.exceptions import ConnectionError


def wait_until_online(timeout=10, snumber=10):
    """ Check if internet connection exits if not wait till sleep number and check again"""
    offline = 1
    while offline:
        try:
            r = get("http://1.1.1.1", timeout=timeout).status_code
        except ConnectionError:
            r = None
        if r == 200:
            print('ONLINE')
            offline = 0
        else:
            print('OFFLINE')
            sleep(snumber)


if __name__ == "__main__":
    wait_until_online()  # timeout and sleep time set to 10 secs by default
