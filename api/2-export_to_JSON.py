#!/usr/bin/python3
"""
A Python script that exports data in JSON format
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'

    todo_response = requests.get(url + f'{employee_id}/todos')
    todos = todo_response.json()

    user_response = requests.get(url + f'{employee_id}')
    user = user_response.json()
    employee_name = user['username']

    user_data = []
    for todo in todos:
        if todo['userId'] == int(employee_id):
            user_data.append(todo)

    user_list = []
    for todo in user_data:
        user_list.append({'task': todo['title'],
                          'completed': todo['completed'],
                          'username': employee_name})

    with open(f'{employee_id}.json', 'w') as file:
        json.dump({f'{employee_id}': user_list}, file)
