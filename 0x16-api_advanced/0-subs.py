#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, timeout=10, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = data['data']['subscribers']
    else:
        count = 0
    return count
