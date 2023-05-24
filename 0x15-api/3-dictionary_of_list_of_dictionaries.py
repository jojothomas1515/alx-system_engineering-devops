#!/usr/bin/python3

"""Rest Api."""

import json
import requests
import sys


def get_user_task(username: str, uid: int):
    """Get formated user task."""

    print(uid)
    info = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(uid))
    todos = info.json()
    todo_fm = list(
        map(
            lambda task: {"username": username,
                          "task": task['title'],
                          "completed": task['completed']},
            todos)
    )

    return todo_fm


def get_info_to_json():
    """Search for a user and all tasks than save it in a json file."""
    users = requests.get("https://jsonplaceholder.typicode.com/users")

    result = {}

    for user in users.json():
        result.update({user['id']: get_user_task(user['username'],
                                                 int(user['id']))})

    with open("todo_all_employees.json", "w") as f:
        json.dump(result, f)


if __name__ == '__main__':
    get_info_to_json()
