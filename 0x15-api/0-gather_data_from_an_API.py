#!/usr/bin/python3
''' A module returns information about his/her TODO list progress
for a given employee ID'''
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}?_embed=todos'
    r = requests.get(url)
    respond_dict = json.loads(r.text)
    
    name = respond_dict.get('name')
    todos = respond_dict.get('todos')
    completed = []
    for task in todos:
        if task.get('completed'):
            completed.append(task.get('title'))
    
    print(f"Employee {name} is done with tasks({len(completed)}/{len(todos)}):")
    for task in completed:
        print(f"\t {task}")
