#!/usr/bin/python3

"""Rest Api."""

import requests
import sys


def get_info(user_id: int):
    """
    Search for a user and print out all completed tasks.

    args:
        user_id: the id if the user to search for
    """
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    info = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id))
    name = user.json()['name']
    counts = len(info.json())
    completed = list(
        filter(
            lambda x: True if x['completed'] is True else False,
            info.json())
    )
    comp_count = len(completed)
    output = "Employee {} is done with tasks({}/{}):"
    print(output.format(name, comp_count, counts))
    for task in completed:
        print("\t {}".format(task['title']))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage {} <user_id>"
              .format(__file__))
    else:
        get_info(int(sys.argv[1]))
