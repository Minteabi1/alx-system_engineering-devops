#!/usr/bin/python3
""" 1-top_ten.py  """


import requests


def top_ten(subreddit):
    """top 10 """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in range(10):
            print(response.json()['data']['children'][i]['data']['title'])
    if response.status_code == 404:
        print('None')
