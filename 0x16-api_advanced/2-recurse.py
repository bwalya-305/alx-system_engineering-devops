#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list of hot article titles

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list): A list of hot article titles (default: [])
        after (str): The name of the last article on the previous page (default: None)

    Returns:
        list: A list of hot article titles, or None if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-app/0.0.1"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
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

