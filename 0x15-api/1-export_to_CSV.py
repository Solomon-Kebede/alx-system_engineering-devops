#!/usr/bin/python3

'''
-Using what you did in the task #0, extend your Python script to export data
in the CSV format.

Requirements:
    -Records all tasks that are owned by this employee
    -Format must be:
    `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
    -File name must be: `USER_ID.csv`
'''

import csv
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
        filename = '{}.csv'.format(employee_id)
        username = employee_data.get('username')
        with open(filename, 'w', newline='') as csv_file:
            csvWriter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for employee_todo in employee_todos:
                user_id = employee_todo.get('userId')
                completed = employee_todo.get('completed')
                task_title = employee_todo.get('title')
                csvWriter.writerow([user_id, username, completed, task_title])
