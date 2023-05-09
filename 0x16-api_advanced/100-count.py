#!/usr/bin/python3
"""Count Words"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Count Words"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    if word_list == []:
        return None
    if after is None:
        response = requests.get(url, headers=headers)
    else:
        response = requests.get(url, headers=headers, params={'after': after})

    if response.status_code == 200:
        for i in response.json()['data']['children']:
            hot_list.append(i['data']['title'])
        after = response.json()['data']['after']
        if after is None:
            word_dic = {}
            for word in word_list:
                word_dic[word] = 0
            for title in hot_list:
                for word in word_list:
                    word_dic[word] += title.lower().split().count(word.lower())
            for word in sorted(word_dic, key=word_dic.get, reverse=True):
                if word_dic[word] != 0:
                    print("{}: {}".format(word, word_dic[word]))
            return None
        return count_words(subreddit, word_list, hot_list, after)
    if response.status_code == 404:
        return None
