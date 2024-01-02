#!/usr/bin/python3

"""Using REST API, returns information about employee TODO list progress."""

import json
import requests

if __name__ == "__main__":
    all_users_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetching data for all employees
    all_users_response = requests.get(all_users_url)
    all_users_response.raise_for_status()
    all_users = all_users_response.json()

    # Prepare data for all employees in JSON format
    data = {}

    for user in all_users:
        user_id = str(user['id'])
        user_todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
        )
        user_todos_response = requests.get(user_todos_url)
        user_todos_response.raise_for_status()
        user_todos = user_todos_response.json()

        data[user_id] = []

        for todo in user_todos:
            task_completed = True if todo['completed'] else False
            data[user_id].append({
                "username": user['username'],
                "task": todo['title'],
                "completed": task_completed
            })

    # Writing data to the JSON file
    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
