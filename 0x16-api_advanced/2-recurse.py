#!/usr/bin/python3
""" Recurse """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recurse """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    if after is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, params={'after': after})

    if response.status_code == 200:
        for i in response.json()['data']['children']:
            hot_list.append(i['data']['title'])
        after = response.json()['data']['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    if response.status_code == 404:
        return None
