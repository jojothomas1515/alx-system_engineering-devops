#!/usr/bin/python3

""" Subreddit subscribers."""

import requests


def top_ten(subreddit):
    """
    Get the Number of subcribers in a subreddit.

    Args:
        subreddit (str): the subreddit to get the info of
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            allow_redirects=False,
                            headers={'User-Agent': 'Mozilla/5.0'})
    if response.status_code == 200:
        data = response.json()
        for post in data.get('data').get('children')[:10]:
            print(str(post.get('data').get('title')))
    else:
        print(None)
