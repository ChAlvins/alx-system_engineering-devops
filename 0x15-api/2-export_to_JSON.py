#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports data in the CSV format
"""
import json
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
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                   "task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": user_name
                                   })
        with open('{}.json'.format(user_id), 'w') as jsonfile:
            json.dump(dictionary, jsonfile)
