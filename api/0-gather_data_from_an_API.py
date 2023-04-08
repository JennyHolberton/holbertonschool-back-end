#!/usr/bin/python3
"""
A Python script that, for a given employee ID,
returns information about their TODO list progress
"""

import requests
import json
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'

    todo_response = requests.get(url + f'{employee_id}/todos')
    todos = todo_response.json()

    user_response = requests.get(url + f'{employee_id}')
    user = user_response.json()
    name = user['username']

    total_tasks = len(todos)
    com_tasks = 0
    task_titles = []

    for todo in todos:
        if todo['completed']:
            com_tasks = com_tasks + 1
            task_titles.append(todo['title'])

    print(f'Employee {name} is done with tasks({com_tasks}/{total_tasks}):')
    for titles in task_titles:
        print(f'\t {titles}')
