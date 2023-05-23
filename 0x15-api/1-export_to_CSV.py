#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports data in the CSV format
"""
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    tasks = response.json()
    with open('{}.csv'.format(user_id), 'w') as csvfile:
        for task in tasks:
            csvfile.write('"{}","{}","{}","{}"\n'.format(user_id, user_name,
                          task.get('completed'), task.get('title')))
