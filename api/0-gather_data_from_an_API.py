#!/usr/bin/python3
"""
A Python script that, for a given employee ID,
returns information about their TODO list progress
"""
import requests
import json
import sys

employee_id = sys.argv[1]
todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
todos = todo_response.json()

user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
user = user_response.json()
employee_name = user['username']

total_tasks = len(todos)
completed_tasks = 0
task_titles = []

for todo in todos:
    if todo['completed']:
        completed_tasks = completed_tasks + 1
        task_titles.append(todo['title'])

print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')
for titles in task_titles:
    print(f'\t {titles}')
