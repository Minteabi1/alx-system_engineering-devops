#!/usr/bin/python3
""" 0-subs.py - returns the number of subscribers for a given subreddit"""


import requests


def number_of_subscribers(subreddit):
    """ number_of_subscribers - returns the number of subscribers for a given
    subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    if response.status_code == 404:
        return 0
