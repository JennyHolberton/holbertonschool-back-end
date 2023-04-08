#!/usr/bin/python3
"""
A Python script that exports data in JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'

    user_response = requests.get(url)
    users = user_response.json()

    all_data = {}

    for user in users:
        employee_id = str(user['id'])
        todo_response = requests.get(url + f'{employee_id}/todos')
        todos = todo_response.json()

        user_data = []
        for todo in todos:
            user_data.append({'username': user['username'],
                              'task': todo['title'],
                              'completed': todo['completed']})
        all_data[employee_id] = user_data

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_data, file)
