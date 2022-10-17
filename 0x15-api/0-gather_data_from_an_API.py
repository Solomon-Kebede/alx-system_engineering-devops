#!/usr/bin/python3

'''
Write a Python(3.4.3) script that, using
this [REST API](https://jsonplaceholder.typicode.com/), for a given
employee ID, returns information about his/her TODO list progress.

Requirements:
    -You must use `urllib` or `requests` module
    -The script must accept an integer as a parameter, which is the employee ID
    -The script must display on the standard output the employee TODO list
    progress in this exact format:
        -First line: `Employee EMPLOYEE_NAME is done with tasks\
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
            -`EMPLOYEE_NAME`: name of the employee
            -`NUMBER_OF_DONE_TASKS`: number of completed tasks
            -`TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum
            of completed and non-completed tasks
        -Second and N next lines display the title of completed tasks:
        `TASK_TITLE` (with 1 tabulation and 1 space before the `TASK_TITLE`)
'''

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
        string_1 = 'Employee {} is done with tasks({}/{}):'
        employee_id = sys.argv[1]
        employee_todos = retrieve(todos_url, employee_id)
        employee_data = retrieve(user_data_url, employee_id)
        completed = []
        for employee_todo in employee_todos:
            if employee_todo.get('completed') is True:
                completed.append(employee_todo.get('title'))
        print(string_1.format(
            employee_data.get('name'),
            len(completed),
            len(employee_todos)))
        for task in completed:
            print('\t {}'.format(task))
