#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive,
delimited by spaces. Javascript should count as
javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, after="", count=[]):
    """prints the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    results = requests.get(url, params={'after': after},
                           allow_redirects=False)

    if results.status_code == 200:
        xdata = results.json()
        data = xdata['data']['children']

    for topic in (data):
        for word in topic['data']['title'].split():
            for i in range(len(word_list)):
                if word_list[i].lower() == word.lower():
                    count[i] += 1

        after_data = xdata["data"]["after"]
        if after_data is not None:
            count_words(subreddit, word_list, after, count)
        else:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        x = count[i]
                        count[i] = count[j]
                        count[j] = x
                        x = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = x

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
