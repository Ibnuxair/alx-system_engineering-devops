#!/usr/bin/python3

"""Using REST API, returns information about employee TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    base_url = (
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    )
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )

    # Fetch employee data
    response = requests.get(base_url)
    response.raise_for_status()
    employee_data = response.json()

    # Fetch todos of the employee
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    # Filter completed and total tasks
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_task_titles = [task['title'] for task in completed_tasks]

    # Prepare data for JSON format
    data = {
        f'{employee_id}': []
    }

    for todo in todos:
        task_completed = True if todo['completed'] else False
        data[f'{employee_id}'].append({
            "task": todo['title'],
            "completed": task_completed,
            "username": employee_data['username']
        })

    # Writing data to the JSON file
    with open(f'{employee_id}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
