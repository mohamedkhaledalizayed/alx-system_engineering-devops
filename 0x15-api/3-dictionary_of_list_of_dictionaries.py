#!/usr/bin/python3
"""Python script to fetch REST API for todo lists of employees"""

import json
import requests
import sys

if __name__ == '__main__':
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetching users data
    users_resp = requests.get(base_url + "users")
    users_data = users_resp.json()

    users_dict = {}

    # Iterating through users
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Fetching tasks for each user
        todos_resp = requests.get(base_url + f"users/{user_id}/todos")
        tasks_data = todos_resp.json()

        # Creating tasks dictionary for each user
        users_dict[user_id] = []
        for task in tasks_data:
            task_completed_status = task.get('completed')
            task_title = task.get('title')

            # Adding task details to user's dictionary
            users_dict[user_id].append({
                "task": task_title,
                "completed": task_completed_status,
                "username": username
            })

    # Writing data to JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
