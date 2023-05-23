#!/usr/bin/python3

"""Rest Api."""

import csv
import requests
import sys


def get_info_to_csv(user_id: int):
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
    todos = info.json()
    with open("{}.csv".format(user_id), "w") as f:
        handler =  csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            handler.writerow([
                user_id,
                name,
                task['completed'],
                task['title']])


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage {} <user_id>"
              .format(__file__))
    else:
        get_info_to_csv(int(sys.argv[1]))
