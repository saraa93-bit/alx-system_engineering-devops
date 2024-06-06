#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles.
If no results are found for the given subreddit,
the function should return None.
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """prints the titles of all hot articles"""
    global after
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    results = requests.get(url, params={'after': after},
                           allow_redirects=False)

    if results.status_code == 200:
        data = results.json()
        after_data = data["data"]["after"]
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        titles = data["data"]["children"]
        for title in titles:
            hot_list.append(title["data"]["title"])
        return hot_list
    else:
        return (None)
