#!/usr/bin/python3

"""Rest Api."""

import json
import requests
import sys


def get_info_to_csv(user_id: int):
    """
    Search for a user and all tasks than save it in a json file.

    args:
        user_id: the id if the user to search for
    """
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    info = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(user_id))
    name = user.json()['name']
    todos = info.json()
    todo_fm = list(
        map(
            lambda task: {"task": task['title'],
                          "completed": task['completed'],
                          "username": name},
            todos)
    )

    inp = {str(user_id): todo_fm}

    with open("{}.json".format(user_id), "w") as f:
        json.dump(inp, f)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("usage {} <user_id>"
              .format(__file__))
    else:
        get_info_to_csv(int(sys.argv[1]))
