#!/usr/bin/python3

"""Rest Api."""

import json
import requests
import sys


def get_user_task(name: str, uid: int):
    """Get formated user task."""

    info = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(uid))
    todos = info.json()
    todo_fm = list(
        map(
            lambda task: {"username": name,
                          "task": task['title'],
                          "completed": task['completed']},
            todos)
    )

    inp = {str(user_id): todo_fm}


def get_info_to_json():
    """Search for a user and all tasks than save it in a json file."""
    users = requests.get("https://jsonplaceholder.typicode.com/users")

    result = {}

    for user in users.json():
        result.update({str(user_id)}
    
    with open("{}.json".format(user_id), "w") as f:
        json.dump(inp, f)

        
if __name__ == '__main__':
    get_info_to_json()
