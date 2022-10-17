#!/usr/bin/python3

'''
-Using what you did in the task #0, extend your Python script to export data
in the JSON format.
Requirements:
    -Records all tasks from all employees
    -Format must be: `{ "USER_ID": [ {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
    -File name must be: `todo_all_employees.json`
'''

import json
import requests

todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
users_data_url = 'https://jsonplaceholder.typicode.com/users'


def reqjson(url):
    '''Returns dict from a json http repsonse'''
    res = requests.get(url)
    return res.json()

if __name__ == '__main__':
    filename = 'todo_all_employees.json'
    employees_data = reqjson(users_data_url)
    result = {}
    for employee_data in employees_data:
        employee_id = employee_data.get('id')
        result[employee_id] = []
        employee_todos = reqjson(todos_url.format(employee_id))
        for employee_todo in employee_todos:
            task_dict = {}
            task_dict['username'] = employee_data.get('username')
            task_dict['task'] = employee_todo.get('title')
            task_dict['completed'] = employee_todo.get('completed')
            result[employee_id].append(task_dict)
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(result))
