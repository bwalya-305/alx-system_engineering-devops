#!/usr/bin/python3
"""
parses title of all hot articles, and prints a sorted count 
of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, count_dict=None):
    if not count_dict:
        count_dict = Counter()
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if 'data' not in data:
        return
    children = data['data']['children']
    for child in children:
        title = child['data']['title']
        words = title.split()
        for word in words:
            word = word.lower()
            if word in word_list:
                count_dict[word] += 1
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after=after, count_dict=count_dict)
    else:
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print(f'{word}: {count}')

