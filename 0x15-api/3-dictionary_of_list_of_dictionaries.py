#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
exports data in the json format
"""
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        user_name = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                                       "username": user_name,
                                       "task": task.get('title'),
                                       "completed": task.get('completed'),
                                       })
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(dictionary, jsonfile)
