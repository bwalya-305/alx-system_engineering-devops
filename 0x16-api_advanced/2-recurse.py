#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests

def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'xica369'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data["data"]["children"]
    for child in children:
        hot_list.append(child["data"]["title"])
    after = data["data"]["after"]
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list

