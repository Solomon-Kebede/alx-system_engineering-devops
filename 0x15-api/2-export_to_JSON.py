#!/usr/bin/python3

'''
-Using what you did in the task #0, extend your Python script to export data
in the JSON format.
Requirements:
    -Records all tasks that are owned by this employee
    -Format must be:
    `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
    -File name must be: `USER_ID.json`

'''

import json
import requests
import sys

todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
user_data_url = 'https://jsonplaceholder.typicode.com/users/{}'


def retrieve(base_url, employee_id):
    '''Retrieves todos/user data'''
    url = base_url.format(employee_id)
    res = requests.get(url)
    return res.json()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
        employee_todos = retrieve(todos_url, employee_id)
        employee_data = retrieve(user_data_url, employee_id)
        result = {}
        result[employee_id] = []
        filename = '{}.json'.format(employee_id)
        for employee_todo in employee_todos:
            task_dict = {}
            task_dict['task'] = employee_todo.get('title')
            task_dict['completed'] = employee_todo.get('completed')
            task_dict['username'] = employee_data.get('username')
            result[employee_id].append(task_dict)
        with open(filename, 'w') as json_file:
            json_file.write(json.dumps(result))
