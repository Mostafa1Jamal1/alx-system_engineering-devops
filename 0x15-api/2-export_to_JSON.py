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

    username = respond_dict.get('username')
    todos = respond_dict.get('todos')

    task_list = []
    for task in todos:
        task_list.append({"task": task.get('title'),
                          "completed": task.get('completed'),
                          "username": username})

    user_dict = {f"{task.get('userId')}": task_list}
    with open(f"{employee_id}.json", "w") as file1:
        file1.write(json.dumps(user_dict))
