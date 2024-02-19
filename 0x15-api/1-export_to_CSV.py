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

    name = respond_dict.get('username')
    todos = respond_dict.get('todos')

    lines = ""
    for task in todos:
        lines += '"{}","{}","{}","{}"\n'.format(
                task.get('userId'),
                name,
                task.get('completed'),
                task.get('title'))

    with open(f"{employee_id}.csv", "w") as file1:
        file1.write(lines)
