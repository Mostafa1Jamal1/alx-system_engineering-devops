#!/usr/bin/python3
''' A module returns information about his/her TODO list progress
for a given employee ID'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}?_embed=todos".format(
        employee_id)
    r = requests.get(url)
    respond_dict = json.loads(r.text)

    name = respond_dict.get('name')
    todos = respond_dict.get('todos')
    completed = []
    for task in todos:
        if task.get('completed'):
            completed.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed), len(todos)
    ))

    for task in completed:
        print(f"\t {task}")
