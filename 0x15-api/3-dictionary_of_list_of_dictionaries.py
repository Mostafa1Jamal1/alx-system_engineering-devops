#!/usr/bin/python3
''' A module returns information about his/her TODO list progress
for a given employee ID'''
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/?_embed=todos"
    r = requests.get(url)
    respond_dict = json.loads(r.text)

    users_dict = {}

    for user in respond_dict:
        username = user.get('username')
        todos = user.get('todos')

        task_list = []
        for task in todos:
            task_list.append({"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": username})

        users_dict[f"{task.get('userId')}"] = task_list

    with open("todo_all_employees.json", "w") as file1:
        file1.write(json.dumps(users_dict))
