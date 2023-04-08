#!/usr/bin/python3
"""
A Python script that exports data in CSV format
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
    name = user['username']

    with open(f'{employee_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([todo['userId'], name,
                             todo['completed'], todo['title']])
