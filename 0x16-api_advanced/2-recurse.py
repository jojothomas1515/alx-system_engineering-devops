#!/usr/bin/python3

""" Subreddit recurse."""

import requests


def recurse(subreddit, hot_list=''):
    """
    Get the Number of subcribers in a subreddit.

    Args:
        subreddit (str): the subreddit to get the info of
    """
    if hot_list is None:
        return (0)
    url = "https://www.reddit.com/r/{:s}/hot.json?after={:s}".format(subreddit,
                                                                     hot_list)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        data = response.json()
        after = data.get('data').get('after')
        return len(data.get('data').get('children')) + \
            recurse(subreddit, after)

    else:
        return (None)
