#!/usr/bin/python3
"""Count Words"""
#!/usr/bin/python3
"""Count Words"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Count Words"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    if not word_list:
        return None

    session = requests.Session()

    while True:
        params = {'limit': 100}
        if after:
            params['after'] = after

        response = session.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()['data']
            hot_list.extend([post['data']['title'] for post in data['children']])
            after = data['after']

            if not after:
                word_dict = {word: 0 for word in word_list}
                for title in hot_list:
                    for word in word_list:
                        word_dict[word] += title.lower().split().count(word.lower())
                for word, count in sorted(word_dict.items(), key=lambda x: x[1], reverse=True):
                    if count != 0:
                        print(f"{word}: {count}")
                break
        elif response.status_code == 404:
            return None
