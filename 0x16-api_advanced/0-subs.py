#!/usr/bin/python3

""" Subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """
    Get the Number of subcribers in a subreddit.

    Args:
        subreddit (str): the subreddit to get the info of
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        data = response.json()
        subscibers_count = data.get("data").get("subscribers")
        return (subscibers_count)
    return (0)
