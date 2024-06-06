#!/usr/bin/python3

"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, timeout=10,
                            params={"limit": 9}, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = data['data']['children']
        for i in range(0, 10):
            print(count[i]['data']['title'])
    else:
        print('None')
