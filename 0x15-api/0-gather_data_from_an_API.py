#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    response = get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId)
    response = get(url)
    tasks = response.json()
    number_of_done_tasks = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            number_of_done_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, number_of_done_tasks, len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
