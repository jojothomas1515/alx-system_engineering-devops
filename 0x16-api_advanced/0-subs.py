#!/usr/bin/python3

""" Subreddit subscribers."""

import requests
import json


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
    print(response.history)
    if response.status_code == 200:
        data = response.json()
        subscibers_count = data.get("data").get("subscribers")
        return (subscibers_count)
    else:
        return (0)


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 2:
        print("This program only accepts one parameter")
        exit(-1)
    print(number_of_subscribers(argv[1]))
